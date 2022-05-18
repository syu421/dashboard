from flask import Flask
app = Flask(__name__, static_folder='.', static_url_path='')
@app.route('/')
def index():
    return app.send_static_file('index.html')

#127.0.0.1:8000/dashboard
@app.route('/dashboard')
def dashboard():
    return app.send_static_file('./dashboard/index.html')

app.run(port=8000, debug=True)