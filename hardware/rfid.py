from time import sleep
from mfrc522 impoort SimpleMFRC522 as mfr
import json 

reader = mfr()

uid = {}

with open('uid.json', 'r') as f:
    uid = json.load(
