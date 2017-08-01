import pygame

class AssetManager():
    def __init__(self, root = ''):
        self.root = root
        self.images = {}

    def load(self, path):
        if self.images[path]:
            return self.images[path]
        self.images[path] = pygame.image.load(self.root + path)

    def box(self, size, color = (255, 255, 255)):
        b = pygame.Surface(size)
        b.fill(color)
        return b
