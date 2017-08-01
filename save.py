#import modules for file management
import json
import os
import gzip

#set program directory where files will all be saved
directory = 'Files/'

#return a list of world files from the directory
def getSaves():
    #list to return
    l = []

    #loop through each file
    for f in os.listdir(directory):
        #check if a world file
        if f.find('.world') >= 0:
            #remove the world extension for list
            l.append(f[0:f.find('.world')])
    #reutrn list
    return l

#class for all save files
class Save():
    #make a new file with given name, if name is none, a settings file will be made
    def __init__(self, name = None):
        #check is a name is given
        if name:
            #get file locations from name and make empty game object
            self.location = os.path.join(directory, name+'.world.gz')
            self.game = None

        #if no name, make settings file
        else:
            #set location and initialaize with default settings values
            self.location = os.path.join(directory, 'settings.json.gz')
            self.initSettings()

        #load file to overide defaults if file exists
        self.load()

    #det defaults settings if a settings file
    def initSettings(self):
        self.lastIP = '127.0.0.1'
        self.port = 6900
        self.fullscreen = False
        self.online = False
        self.female = True
        self.name = 'Bella'
        self.color = ((0,0,255), 'Blue')
        self.seed = 0
    
    #load file values
    def load(self):
        #try to open files and decompress
        try:
            with gzip.open(self.location, 'rb') as f:
                self.__dict__ = json.loads(f.read().decode())

        #if unable to open file, do nothing
        except:
            print('Failed to load "'+self.location+'"')

    #save file as a gzipped json file
    def save(self):
        with gzip.open(self.location, 'wb') as f:
            f.write(json.dumps(self.__dict__).encode())

    #delete a file from disk
    def delete(self):
        os.remove(self.location)
