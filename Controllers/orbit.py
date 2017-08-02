import math

class Orbit():
    def __init__(self, r, f):
        self.frame = 0
        self.f = f
        self.r = r
        self.node = None

    def update(self):
        self.node.setXY(self.r*math.cos(self.frame/self.f), self.r*math.sin(self.frame/self.f))
        self.frame += 1
