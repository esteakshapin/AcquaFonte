from pymongo import MongoClient
from flask import Flask, render_template, request
import ssl

app = Flask(__name__)
app.secret_key = '6yTWFOE7j05WpVr8ic'

client = MongoClient('mongodb://Shapin:Shapin@cluster0-shard-00-00-lnqyp.mongodb.net:27017,cluster0-shard-00-01-lnqyp.mongodb.net:27017,cluster0-shard-00-02-lnqyp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority')

db = client['AqcuaFonte']
users = db['users']

# Home Page
@app.route('/', methods=['GET'])
def home_page():
  return render_template('index.html')

# Find_Water Page
@app.route('/find_water', methods=['GET'])
def find_water_page():
  return render_template('find_water.html')

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
    return 'sucess'



  


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)