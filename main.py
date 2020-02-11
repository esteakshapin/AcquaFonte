from flask import Flask, render_template

app = Flask(__name__)

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
@app.route('/log_in', methods=['GET'])
def log_in_page():
  return 


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)