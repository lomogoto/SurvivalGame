#class for gui node elements
class GuiNode():
    def __init__(self, name):
        self.name = name
        self.pos = [0, 0]
        self.controls = []

    def setLocation(x, y):
        self.pos = [x, y]

    def move(x, y):
        self.pos[0] += x
        self.pos[1] += y

    def addControl(control):
        self.controls.append(control)
