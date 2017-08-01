#!/usr/bin/env python3

#import pygame for graphics
import pygame

#import project
import node
import camera
import graph
import inputmanager

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
        self.cam = camera.Camera(self.scene, (16,12))
        self.cam2d = camera.Camera(self.scene, (1,1))
        self.graph = graph.Graph(self.cam)
        self.graph2d = graph.Graph(self.cam2d)
        self.inputManager = inputmanager.InputManager()

    #initialize the game
    def initGame(self):
        self.inputManager.register('back', self.quit)

    #start the game
    def start(self):
        self.running = True
        while self.running:
            self.inputManager.update()
            self.graph.update()
            self.graph2d.update()
            self.graph.render()
            self.graph2d.render()
            self.clock.tick(self.fps)
            pygame.display.update()

    #safely exit the game
    def quit(self, state):
        self.running = False

#build and run the app
app = Main()
app.start()
