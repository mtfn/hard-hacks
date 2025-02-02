from time import sleep
from mfrc522 import SimpleMFRC522 as mfr
import json
import socketio
import eventlet
import eventlet.wsgi


# app = Flask(__name__)
sio = socketio.Server()
app = socketio.WSGIApp(sio)
rdr = mfr()

dic = {
    "584188633845":"harsha",
    "584189904231": "andy",
    "584185153698": "matt"
}

@sio.event
def connect(sid, environ):
    print('connected')
    id, text = rdr.read() 
    print(dic[str(id)])
    sio.emit('idScanned', dic[str(id)], room=sid)

if __name__ == "__main__":
    #app.run(port=8080)

    eventlet.wsgi.server(eventlet.listen(('', 8080)), app)
