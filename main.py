#!/usr/bin/env python3

#import pygame for graphics
import pygame

#import project
import node
import camera
import graph

#main class
class Main():
    #constants
    res = 480
    fps = 60

    #initialize the game
    def __init__(self):
        self.initPygame(False)
        self.initEngine()
        self.initGame()

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
        self.scene = pygame.Surface((res, res*self.h/self.w))

    def initEngine(self):
        self.cam = camera.Camera(self.scene, (16,12))
        self.cam2d = camera.Camera(self.scene, (1,1))
        self.graph = graph.Graph(cam)
        self.graph2d = graph.Graph(cam2d)

    def initGame(self):
        pass

