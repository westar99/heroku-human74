from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    return 'random:<h2>'+str(random.random())+'</h2>'

@app.route('/create/')
def create():
    return 'create'

@app.route('/read/<id>/')
def read(id):
    print(id)
    return 'read:'+id

app.run(debug=True)