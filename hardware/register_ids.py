from time import sleep
from mfrc522 import SimpleMFRC522 as mfr
import json


reader = mfr()

uid = {}

try:
    while True:
        print("waiting for read")
    
        id, text = reader.read()
        print(id)

        uid[id] = input("Enter name: ")

except KeyboardInterrupt:
    if input('q!'):
        exit()

    with open('uid.json', 'w') as file:
        json.dump(uid, file, indent=4)
