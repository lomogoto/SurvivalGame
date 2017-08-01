import math

class Orbit():
    def __init__(self, f):
        self.frame = 0
        self.f = f
        self.node = None

    def update(self):
        self.node.setXY(math.sin(self.frame/self.f), math.cos(self.frame/self.f))
        self.frame += 1
