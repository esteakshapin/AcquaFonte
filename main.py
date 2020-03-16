#import fixpath
from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify, session
import ssl
# import csv
import math
from datetime import datetime
from google.cloud import storage
import pickle
from pictureclass import myFileList
import random
import string

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
# from threading import Thread

app = Flask(__name__)
app.secret_key = '6yTWFOE7j05WpVr8ic'

client = MongoClient('mongodb://Shapin:Shapin@cluster0-shard-00-00-lnqyp.mongodb.net:27017,cluster0-shard-00-01-lnqyp.mongodb.net:27017,cluster0-shard-00-02-lnqyp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority', ssl_cert_reqs=ssl.CERT_NONE)

storage_client = storage.Client()#gcloud storage, #making sure that bucket exists
#bucket per our defined regions
bucket_name = "fountain-images"
bucket = storage_client.get_bucket(bucket_name)
print(bucket.name)

db = client['AqcuaFonte']
users = db['users']
markers = db['markers']
unconfirmed_markers = db['unconfirmed_markers']


#finding markers in range
def get_fountains_in_range(lat, lon, distance_range):
  earth_radius = 3958.75
  lat2 = lat
  lon2 = lon
  list_return = []

  list_of_markers = markers.find({})

  for docs in list_of_markers:
    lat1 = docs['lat']
    lon1 = docs['lon']

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2 - lon1)

    sinDlat = math.sin(dlat/ 2)
    sinDlon = math.sin(dlon / 2)

    a = math.pow(sinDlat, 2) + math.pow(sinDlon, 2) * math.cos(math.radians(lat1)) * math.cos(math.radians(lat2))

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    dist = earth_radius * c

    if (dist < distance_range):
      docs['dist'] = dist
      list_return.append(docs)

  return list_return

#adding header to disable caching -- REMOVE WHEN DEPLOYING SITE
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

# Home Page
@app.route('/', methods=['GET'])
def home_page():
  return render_template('index.html')

# Find_Water Page
@app.route('/find_water', methods=['GET'])
def find_water_page():
  if (session.get('logged_in') == None):
    session['logged_in'] = False
  return render_template('find_water.html', logged_in=session.get('logged_in'))

# get markers
@app.route('/get_markers', methods=['GET'])
def get_markers():
  lat = float(request.args['lat'])
  lon = float(request.args['lon'])
  dist_range = float(request.args['dist_range'])

  h = get_fountains_in_range(lat,lon,dist_range)

  for i in h:
    i.pop('_id')

  return jsonify(h)


def allowed_extension(extension):
    return extension.lower() in ALLOWED_EXTENSIONS

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))



# Add_Location Page
@app.route('/add_location', methods=['GET', 'POST'])
def add_location_page():
    if request.method == 'POST':
        #start add location code
        fountain_name = request.form['fountain_name']
        fountain_comment = request.form['fountain_comment']
        status = request.form['status']
        type = request.form['type']
        rating = request.form['rating']
        lat = float(request.form['lat'])
        lng = float(request.form['lng'])

        if 'fountain_img_input' in request.files and request.files['fountain_img_input'].filename != '': #ask if a img was sent // img is not none type
            print('second level made')
            myFile = request.files['fountain_img_input'] #get image
            fileextension = myFile.filename.rsplit('.', 1)[1]
            if myFile.filename != '' and allowed_extension(fileextension): #ask if extention in allowed extensions
                print("#important")

                #adding image to cloud storage
                destination_name = randomString(20)#creating random string for destination file

                #adding image to blob
                blob = bucket.blob(destination_name)

                #uploading blob to bucket
                blob.upload_from_file(myFile)

                #storing public url to access later
                url = blob.public_url

                unconfirmed_markers.insert_one({"name": fountain_name, "lat":lat, "lon":lng, "type": type, "status": status, "ratings": [rating], "comments":[fountain_comment], "pics": [url]})

                print("success")


                #bucket per our defined regions

                # try:
                #     bucket = storage_client.bucket("nyc")#if bucket exist
                #     #pull blob, -> append, release
                #     try: #if blob for fountain exists
                #         blob = bucket.get_blob(str(markerid))
                #         #if it exists unpickle
                #         myClass = pickle.loads(blob)
                #         #package should be a wrapper class with function to append
                #         myClass.addimg(myFile.read) #add our file to object
                #     except:
                #         # if blob doesnt exist, make class, push code
                #         myClass = myFileList([myFile.read])
                #         pass
                #
                #     #now that classes are made / appended too, prepare + push that object to
                #     package = pickle.dumps(myClass)
                #     blob = bucket.blob(str(markerid))
                #     blob.upload_from_string(package)
                #     # blob = bucket.blob(str(markerid) + '/' + len(fountain))
                #     # blob.upload_from_file(myFile.read())
                #
                # except: #bucket and it associated blob doesnt exist
                #     bucket = "nyc"
                #     bucket = storage_client.create_bucket(bucket)#make bucket
                #     bucket.location = "US-EAST4" #maybe lowercase
                #     bucket.storage_class = "STANDARD"
                #     myClass = myFileList([myFile.read])
                #     #convert to pickling byte object
                #     package = pickle.dumps(myClass)
                #     blob = bucket.blob(str(markerid))
                #     blob.upload_from_string(package)


                return "success"
            return "Error. Please check to make sure the file you updated is an image"
    return render_template('add_location.html')

# @app.route('/test', methods=['GET'])
# def test():
#     try:
#         bucket = storage_client.bucket("test")#if bucket exist
#         assert isinstance(bucket, Bucket)
#         #get blob with
#         blob = bucket.blob('testing')
#         blob.download_to_filename('filetest.png')
#     except:
#         print('bucketnotfound')

# Contact Page
@app.route('/contact', methods=['GET'])
def contact_page():
  return render_template('contact.html')

# About_Us Page
@app.route('/about_us', methods=['GET'])
def about_us_page():
  return render_template('about_us.html')

# Log_in Page
@app.route('/log_in', methods=['GET','POST'])
def log_in_page():
  if request.method == 'GET':
    if (session.get('logged_in') == None):
      session['logged_in'] = False
    return render_template('log_in.html', logged_in=session.get('logged_in'), first_name=session.get('first_name'), last_name=session.get('last_name'))

  elif request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    if (users.count_documents({'username':username, 'password': password}) > 0):
        user = users.find({'username':username, 'password':password})
        user = user[0]
        session['first_name'] = user["first_name"]
        session['last_name'] = user["last_name"]
        session['username'] = username
        session['logged_in'] = True
        print('logged in')
        return 'success'
    else:
        print("user not found",username,password)
        return 'failure'

#log_out mechanism
@app.route('/log_out', methods=['POST'])
def log_out():
  session.pop('username')
  session.pop('first_name')
  session.pop('last_name')
  session.pop('logged_in')
  return 'success'

# register mechanism
@app.route('/register', methods=['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    username = request.form['username']
    password = request.form['password']
    confirm_pass = request.form['confirm_pass']
    print(username, password, confirm_pass)
    if (confirm_pass == password):
        if (users.count_documents({'username':username}) > 0):
            print('Username Taken')
            return 'failure'
        else:
            users.insert_one({'username':username, 'password':password, 'first_name':first_name,'last_name':last_name})
            session['first_name'] = first_name
            session['last_name'] = last_name
            session['username'] = username
            session['logged_in'] = True
            print('added new user')
            return 'success'
    else:
        print('passwords do not match up! Try Again')
        return 'failure'

# def run():
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)

#def keep_alive():
#    t = Thread(target=run)
#    t.start()

#keep_alive()
