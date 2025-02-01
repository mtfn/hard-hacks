from time import sleep
from mfrc522 import SimpleMFRC522 as mfr
import csv


reader = mfr()

uid = {}

try:
    while True:
        print("waiting for read")
    
        id, text = reader.read()
        print(id)

        uid[input("Enter name: ")] = id

except KeyboardInterrupt:
    if input('q!'):
        exit()

    with open('uid.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['name', 'uid'])
        writer.writeheader()
        writer.writerows(uid)
