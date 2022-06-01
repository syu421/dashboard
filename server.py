import json
from flask import Flask, jsonify
app = Flask(__name__, static_folder='.', static_url_path='')
@app.route('/')
def index():
    return app.send_static_file('index.html')

#127.0.0.1:8000/dashboard
@app.route('/dashboard')
def dashboard():
    return app.send_static_file('./dashboard/index.html')

import database
@app.route('/getall')
def get_value():
    res = database.get_gps()
    webres = json.loads(res)
    return jsonify(webres) 

app.run(port=8000, debug=True)