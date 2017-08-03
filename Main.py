#!/usr/bin/env python3

#import pygame for graphics
import pygame

#import project
from Engine import Node
from Engine import Camera
from Engine import InputManager
from Engine import FileManager
from Factories import Menu

#main class
class Main():
    #initialize the game
    def __init__(self):
        #playback constants
        self.res = 320
        self.fps = 60

        #initialize pygame
        pygame.init()

        #try to load settings or use defaults
        try:
            self.settings = FileManager.load('Data/settings.json.gz')
        except KeyError:
            self.settings = {'dimentions' : [960, 540],
                    'color' : [0, 0, 200]}
            FileManager.save('Data/settings.json.gz', self.settings)

        #make windowed or fullscreen
        if self.settings['dimentions'] == [0,0]:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(self.settings['dimentions'])

        #make the screen and clock
        self.clock = pygame.time.Clock()

        #make low resolution surface
        self.scene = pygame.Surface((self.res, self.res*self.screen.get_height()/self.screen.get_width()))

        #make engine related variables
        self.render = Node.Node()
        self.cam = Camera.Camera(self.scene, (16,12))
        self.render.attach(self.cam)

        InputManager.poll()
        InputManager.register('back', self.quit)

        self.initGame()

    #initialize the game
    def initGame(self):
        menuFactory = Menu.Menu(quit)
        self.render.attach(menuFactory.makeMainMenu())

    #start the game
    def start(self):
        self.running = True
        while self.running:
            InputManager.update()
            self.render.update()
            self.cam.render()
            self.clock.tick(self.fps)
            pygame.transform.scale(self.scene, (self.screen.get_width(), self.screen.get_height()), self.screen)
            pygame.display.update()

    #safely exit the game
    def quit(self, state):
        self.running = False
        return Node.Node()

#build and run the app
app = Main()
app.start()
