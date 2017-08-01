#!/usr/bin/env python3

#import pygame for graphics
import pygame

#import project
import node
import camera
import control
import inputmanager
import assetmanager

#main class
class Main():
    #initialize the game
    def __init__(self):
        #initialize variables
        self.res = 480
        self.fps = 60
        self.running = False
        
        #initialize the game in steps
        self.initPygame(False)
        self.initEngine()
        self.initGame()

    #initialize the pygame library
    def initPygame(self, fullscreen):
        #initialize pygame
        pygame.init()

        #make windowed or fullscreen
        if fullscreen:
            self.w = pygame.display.Info().current_w
            self.h = pygame.display.Info().current_h
        else:
            self.w = 800
            self.h = 600

        #make the screen and clock
        self.screen = pygame.display.set_mode((self.w, self.h))
        self.clock = pygame.time.Clock()

        #make low resolution surface
        self.scene = pygame.Surface((self.res, self.res*self.h/self.w))

    #initialize the game engine
    def initEngine(self):
        #make engine related variables
        self.render = node.Node()
        self.cam = camera.Camera(self.scene, (16,12))
        self.render.attach(self.cam)

        self.inputManager = inputmanager.InputManager()
        self.assetManager = assetmanager.AssetManager('Assets/')

        self.inputManager.register('back', self.quit)

    #initialize the game
    def initGame(self):
        b = node.Node()
        b.image = self.assetManager.box((8,8))
        b.attachControl(control.Control(120))
        self.render.attach(b)

        b2 = node.Node()
        b2.image = self.assetManager.box((32,32), (255,0,0))
        b2.setDepth(-1)
        b2.attachControl(control.Control(40))
        b.attach(b2)

    #start the game
    def start(self):
        self.running = True
        while self.running:
            self.inputManager.update()
            self.render.update()
            self.cam.render()
            self.clock.tick(self.fps)
            pygame.transform.scale(self.scene, (self.w, self.h), self.screen)
            pygame.display.update()

    #safely exit the game
    def quit(self, state):
        self.running = False

#build and run the app
app = Main()
app.start()
