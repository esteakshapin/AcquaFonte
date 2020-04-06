#import fixpath
from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import ssl
# import csv
import math
from datetime import datetime
from google.cloud import storage
import pickle
from pictureclass import myFileList
from bson.objectid import ObjectId
from datetime import datetime
import random
import string
import os

#setting google GOOGLE_APPLICATION_CREDENTIALS
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="Acqua Fonte-2a34c22c7ffe.json"

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
# from threading import Thread

app = Flask(__name__)
app.secret_key = '6yTWFOE7j05WpVr8ic'

client = MongoClient('mongodb://Shapin:Shapin@cluster0-shard-00-00-lnqyp.mongodb.net:27017,cluster0-shard-00-01-lnqyp.mongodb.net:27017,cluster0-shard-00-02-lnqyp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority', ssl_cert_reqs=ssl.CERT_NONE)

db = client['AqcuaFonte']
users = db['users']
markers = db['markers']
unconfirmed_markers = db['unconfirmed_markers']

#google storage variable
bucket_name = "fountain-images"
bucket_php_name = "user-php"

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
      docs['_id'] = str(docs['_id'])
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
  if (session.get('logged_in')):
      return render_template('index.html', logged_in=session.get('logged_in'), username=session.get('username'))

  return render_template('index.html')

# Find_Water Page
@app.route('/find_water', methods=['GET'])
def find_water_page():
  if (session.get('logged_in') == None):
    session['logged_in'] = False
  return render_template('find_water.html', logged_in=session.get('logged_in'), username=session.get('username'))

# get markers
@app.route('/get_markers', methods=['GET'])
def get_markers():
  lat = float(request.args['lat'])
  lon = float(request.args['lon'])
  dist_range = float(request.args['dist_range'])

  h = get_fountains_in_range(lat,lon,dist_range)

  # for i in h:
  #   i.pop('_id')

  return jsonify(h)


def allowed_extension(extension):
    return extension.lower() in ALLOWED_EXTENSIONS

# def getDetail(string, seperator):
#     throw, k, keep = string.partition(seperator)
#     if ',' in keep:
#         value, throw, leftover = keep.partition(',')
#     else:
#         value, throw, leftover = keep.partition('}')
#     value = value.strip(')\'\": ')
#     return value, leftover

# Add_Location Page
@app.route('/add_location', methods=['GET', 'POST'])
def add_location_page():
    if request.method == 'POST':
        status = request.form['status']
        rating = request.form['rating']
        fountain_comment = request.form['fountain_comment']
        if "_id" in request.form:
            fountainId = request.form['_id']
            print(fountainId)
            print(status)
            print(rating)
            print(fountain_comment)
            thisMarker = markers.update_one(
                {"_id": ObjectId(fountainId)},
                # {'$currentDate': {datetime.now(): True}},
                {
                    '$set': {
                        'status': status
                        }
                    ,
                    '$push': {
                        'comments': fountain_comment,
                        'ratings': rating
                        }

                },
                upsert=True ).raw_result#, {'rating': 1}
            print(thisMarker) #### returning None, no object found
            if thisMarker['updateExisting'] == True:
                return ('Fountian info edited')
            else:
                return ('Server side error, Changes thrown away') #-----------------------------------------------------------------------------


        fountain_name = request.form['fountain_name']
        ftype = request.form['type']
        lat = float(request.form['lat'])
        lng = float(request.form['lng'])
        if 'fountain_img_input' in request.files and request.files['fountain_img_input'].filename != '': #ask if a img was sent // img is not none type
            print('second level made')
            myFile = request.files['fountain_img_input'] #get image
            fileextension = myFile.filename.rsplit('.', 1)[1]
            if myFile.filename != '' and allowed_extension(fileextension): #ask if extention in allowed extensions
                print("#important")
                # print(type(myFile.read()))
                #bucket per our defined regions
                gcs  = storage.Client()#gcloud storage, #making sure that bucket exists
                destination_name = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(20))
                bucket = gcs.get_bucket(bucket_name)
                blob = bucket.blob(destination_name)
                blob.upload_from_string(
                    myFile.read(),
                    content_type=myFile.content_type
                )
                blob.make_public()#allowing for the url to return an image
                # The public URL can be used to directly access the uploaded file via HTTP.
                url = blob.public_url
                #adding fountain to unconfirmed database
                unconfirmed_markers.insert_one({"name": fountain_name, "lat":lat, "lon":lng, "type": ftype, "status": status, "ratings": [rating], "comments":[fountain_comment], "pics": [url]})
                return "success"
            return "Error. Please check to make sure the file you updated is an image"
        else:
            #adding fountain to unconfirmed database
            unconfirmed_markers.insert_one({"name": fountain_name, "lat":lat, "lon":lng, "type": ftype, "status": status, "ratings": [rating], "comments":[fountain_comment]})
            return "success"
    #reponse to get
    if (session.get('logged_in')):
        if ('fountain' in request.args):
            # build try except
            fDetails = request.args['fountain']
            fDetails = eval(fDetails)
            fDetails['_id'] = str(fDetails['_id'])
            print(fDetails.items())
            reDetails = []
            ratings = fDetails['ratings']
            if len(ratings) != 0:
                averageRating = sum(ratings) / len(ratings)
                averageRating = round(averageRating)
            else:
                averageRating = 0
            fDetails['ratings'] = averageRating
            for i,values in fDetails.items():
                reDetails.append([i, values])
            print(reDetails)
            return render_template('add_location.html', username=session.get('username'), thisFountain=reDetails)
        else:
            return render_template('add_location.html', username=session.get('username'))
    else:
        return redirect(url_for('log_in_page'))

#editing markers
@app.route('/edit_location', methods=['GET'])
def edit_location():
    id = str(request.args['_id'])
    fountain = markers.find_one({"_id": ObjectId(id)})
    if fountain == None:
        return "failure; fountain could not be found please try again"
    print(fountain)
    return redirect(url_for('add_location_page', fountain=fountain))

# Contact Page
@app.route('/contact', methods=['GET'])
def contact_page():
  if (session.get('logged_in')):
    return render_template('contact.html', username=session.get('username'))

  return render_template('contact.html')

# About_Us Page
@app.route('/about_us', methods=['GET'])
def about_us_page():
  if (session.get('logged_in')):
    return render_template('about_us.html', username=session.get('username'))

  return render_template('about_us.html')



# Account page
@app.route('/myAccount', methods=['GET', 'POST'])
def myAccount():
    if request.method == 'POST':
        print('post hello')
        updated_user = request.form['newUsername'] == "true"
        updated_First = request.form['newFirst'] == "true"
        updated_Last = request.form['newLast'] == "true"
        newPFP = request.form['newPFP'] == "true"

        newUsername = request.form['username']
        newFirst = request.form['firstname']
        newLast = request.form['lastname']
        notchanged = True
        changes = []

        if 'profilepic' in request.files and request.files['profilepic'].filename != '': #ask if a img was sent // img is not none type
            print('file found')
            myFile = request.files['profilepic'] #get image
            fileextension = myFile.filename.rsplit('.', 1)[1]
            if myFile.filename != '' and allowed_extension(fileextension): #ask if extention in allowed extensions
                # print(type(myFile.read()))
                #bucket per our defined regions
                gcs  = storage.Client()#gcloud storage, #making sure that bucket exists
                destination_name = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(20))
                bucket = gcs.get_bucket(bucket_php_name)
                blob = bucket.blob(destination_name)
                blob.upload_from_string(
                    myFile.read(),
                    content_type=myFile.content_type
                )
                blob.make_public()#allowing for the url to return an image
                # The public URL can be used to directly access the uploaded file via HTTP.
                url = blob.public_url
                #adding fountain to unconfirmed database
                users.find_one_and_update({"username": session.get('username')}, {'$set': {"profilepic" : url}})
                notchanged = False
                changes += 'Profile-pic Changed'
                session['profilepic'] =  url

        if updated_user and (users.count_documents({'username':newUsername}) > 0):#ask if the change username is valid
            print('Username Taken')
            return 'Username Taken, Account change halted'

        if updated_First and newFirst and newFirst.strip() != "": #update the user's firstname
            users.find_one_and_update({"username": session.get('username')}, {'$set': {"first_name" : newFirst}})
            notchanged = False
            changes += "\nFirst-name Changed"
            session['first_name'] = newFirst

        if updated_Last and newLast and newLast.strip() != "": #update the user's lastname
            users.find_one_and_update({"username": session.get('username')}, {'$set': {"last_name" : newLast}})
            notchanged = False
            changes += '\nLast-name Changed'
            session['last_name'] = newLast

        if updated_user and newUsername.strip() != "": #update the user's username
            users.find_one_and_update({"username": session.get('username')}, {'$set': {"username" : newUsername}})
            notchanged = False
            changes += '\nUsername Changed'
            session['username'] = newUsername
        print('sending response')

        if notchanged: #if no changes were made // catch all post request
            return "no changes were made, feilds empty"
        else:
            return jsonify(changes)


    if (session.get('logged_in')): #if not none type
        if (session.get('profilepic')):
            return render_template('myAccount.html',profilepic=session.get('profilepic'),logged_in=session.get('logged_in'), first_name=session.get('first_name'), last_name=session.get('last_name'), username=session.get('username'))
        return render_template('myAccount.html',logged_in=session.get('logged_in'), first_name=session.get('first_name'), last_name=session.get('last_name'), username=session.get('username'))
    else:
        return redirect(url_for('log_in_page'))


# Log_in Page
@app.route('/log_in', methods=['GET','POST'])
def log_in_page():
  if request.method == 'GET':
    if (session.get('logged_in') == None):
      session['logged_in'] = False
    return render_template('log_in.html', first_name=session.get('first_name'), last_name=session.get('last_name'))

  elif request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    if (users.count_documents({'username':username, 'password': password}) > 0):
        user = users.find({'username':username, 'password':password})
        user = user[0]
        session['first_name'] = user["first_name"]
        session['last_name'] = user["last_name"]
        session['profilepic'] = user['profilepic'] # does this work?
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
  try:
    session.pop('profilepic')
  except:
    pass

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
            users.insert_one({'username':username, 'password':password, 'first_name':first_name,'last_name':last_name, "profilepic":"https://storage.cloud.google.com/fountain-images/HZKltov0PNSqG0ww5qeD"})
            session['first_name'] = first_name
            session['last_name'] = last_name
            session['username'] = username
            session['profilepic'] = user['profilepic']
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
