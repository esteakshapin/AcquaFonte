from pymongo import MongoClient
from flask import Flask, render_template, request,jsonify
import ssl
# import csv
import math

app = Flask(__name__)
app.secret_key = '6yTWFOE7j05WpVr8ic'

client = MongoClient('mongodb://Shapin:Shapin@cluster0-shard-00-00-lnqyp.mongodb.net:27017,cluster0-shard-00-01-lnqyp.mongodb.net:27017,cluster0-shard-00-02-lnqyp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority', ssl_cert_reqs=ssl.CERT_NONE)

db = client['AqcuaFonte']
users = db['users']
markers = db['markers']


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
  return render_template('find_water.html')

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
  


# Add_Location Page
@app.route('/add_location', methods=['GET'])
def add_location_page():
  return render_template('add_location.html')

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
    return render_template('log_in.html')
  elif request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    if (users.count_documents({'username':username, 'password': password}) > 0):
        print('found user')
        return 'success'
    else:
        print("user not found",username,password)
        return 'failure'

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    confirm_pass = request.form['confirm_pass']
    print(username, password, confirm_pass)
    if (confirm_pass == password):
        if (users.count_documents({'username':username, 'password': password}) > 0):
            print('user already exists please log in')
            return 'failure'
        else:
            users.insert_one({'username':username, 'password':password})
            print(users.find({'username':username, 'password':password}))
            return 'success'
    else:
        print('passwords do not match up! Try Again')
        return 'failure'







if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=False)
