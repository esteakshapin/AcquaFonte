from pymongo import MongoClient
from flask import Flask, render_template, request,jsonify,session
import ssl
# import csv
import math
from datetime import datetime

from threading import Thread

app = Flask(__name__)
app.secret_key = '6yTWFOE7j05WpVr8ic'

client = MongoClient('mongodb://Shapin:Shapin@cluster0-shard-00-00-lnqyp.mongodb.net:27017,cluster0-shard-00-01-lnqyp.mongodb.net:27017,cluster0-shard-00-02-lnqyp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority', ssl_cert_reqs=ssl.CERT_NONE)

db = client['AqcuaFonte']
users = db['users']
markers = db['markers']
visits = db['visits']


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
  ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
  referer_page = request.referrer
  user_agent = request.user_agent.string
  time = datetime.now()

  if (user_agent != 'Mozilla/5.0+(compatible; UptimeRobot/2.0; http://www.uptimerobot.com/)'):
    print({'ip': ip_address, 'time':time})
    visits.insert_one({'ip': ip_address, 'time':time, 'referer_page':referer_page, 'user_agent':user_agent})

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

def run():
  if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)

def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()
