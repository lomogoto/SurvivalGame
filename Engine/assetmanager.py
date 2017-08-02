import pygame

class AssetManager():
    def __init__(self, root = '', colorkey = (255,0,0)):
        self.root = root
        self.images = {}
        self.colorkey = colorkey

    def load(self, path):
        if not path in self.images:
            self.images[path] = pygame.image.load(self.root + path)
            self.images[path].set_colorkey(self.colorkey)
        return self.images[path]

    def box(self, size, color = (255, 255, 255)):
        b = pygame.Surface(size)
        b.fill(color)
        return b

    def text(self, fontpath, string, charwidth = 8):
        font = self.load(fontpath)

        t = pygame.Surface((charwidth*len(string), font.get_height()))
        t.fill(self.colorkey)
        t.set_colorkey(self.colorkey)
        i = 0
        for c in string:
            letter = font.subsurface((charwidth*(ord(c)-65), 0, charwidth, font.get_height()))
            t.blit(letter, (charwidth*i, 0))
            i += 1

        return t
