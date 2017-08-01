#class for all game nodes
class Node():
    def __init__(self, name):
        self.name = name
        self.pos = [0, 0, 0]
        self.controls = {}
        self.image = None

    def getImage(self):
        return self.image

    def setLocation(self, x, y, z):
        self.pos = [x, y]

    def move(self, x, y, z):
        self.pos[0] += x
        self.pos[1] += y

    def attachControl(self, control):
        self.controls[control.getName()] = control
