from time import sleep
from mfrc522 import SimpleMFRC522 as mfr

def return_uid():
    rdr = mfr()

    try:
        while True:
            print("waiting")

            id, text = reader.read()

            print(id)

            return id

        except KeyboardInterrupt:
            return None
