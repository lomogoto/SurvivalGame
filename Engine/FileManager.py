import json
import os
import gzip

files = {}

currentLocation = None

def setSaveFile(location):
    global currentLocation
    currentLocation = location

def getFromSave(key):
    return load(currentLocation)[key]

def save(location, data = None):
    if data:
        files[location] = data

    with gzip.open(location, 'wb') as f:
        f.write(json.dumps(files[location]).encode())

def load(location):
    if not location in files:
        try:
            with gzip.open(location, 'rb') as f:
                files[location] = json.loads(f.read().decode())
        except:
            print('Unable to load "' + location + '"')
    return files[location]

def delete(location):
    del files[location]
    os.remove(location)
