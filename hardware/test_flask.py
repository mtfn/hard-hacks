from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from time import sleep
from mfrc522 import SimpleMFRC522 as mf

import json

rdr = mf()

uid = {}

with open('uid.json', 'r') as f:
    uid = json.load(f)
    print(uid)

app = Flask(__name__)

app.config['SECRET KEY'] = 'secret'
CORS(app,resources={r"/*":{"origins":"*"}})
socketio = SocketIO(app, cors_allowed_origins="*")

values = {
    'slider1': 25,
    'slider2': 0,
}

@app.route('/')
def index():
    return render_template('index.html',**values)

@socketio.on('connect')
def test_connect():
    #    emit('idScanned',  {'data':'Lets dance'})
    print("con") 
    id, text = rdr.read()

    print(id)

    emit('idScanned', uid[str(id)]) 
    
    print("test")



@socketio.on('Slider value changed')
def value_changed(message):
    values[message['who']] = message['data']
    emit('update value', message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, port=8080)
