import pygame

colorkey = (255,0,0)
images = {}

def load(path):
    if not path in images:
        images[path] = pygame.image.load(path)
        images[path].set_colorkey(colorkey)
    return images[path]

def box(size, color = (255, 255, 255)):
    b = pygame.Surface(size)
    b.fill(color)
    return b

def text(fontpath, string, charwidth = 8):
    font = load(fontpath)

    t = pygame.Surface((charwidth*len(string), font.get_height()))
    t.fill(colorkey)
    t.set_colorkey(colorkey)
    i = 0
    for c in string:
        if ord(c) > 64:
            letter = font.subsurface((charwidth*(ord(c)-65), 0, charwidth, font.get_height()))
            t.blit(letter, (charwidth*i, 0))
        elif ord(c) >= 47:
            number = font.subsurface((charwidth*(ord(c)-22), 0, charwidth, font.get_height()))
            t.blit(number, (charwidth*i, 0))
        i += 1

    return t
