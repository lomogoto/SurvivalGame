#class for all game nodes
class Node():
    def __init__(self):
        self.pos = [0, 0, 0]
        self.controls = []
        self.image = None
        self.parent = None
        self.children = []

    def attach(self, child):
        if child.parent:
            child.parent.detatch(child)
        child.parent = self
        self.children.append(child)

    def detach(self, child):
        child.parent = None
        self.children.remove(child)

    def attachControl(self, control):
        control.node = self
        self.controls.append(control)

    def detachControl(self, control):
        control.node = None
        self.controls.remove(control)

    def setDepth(self, z):
        self.pos[2] = z

    def setXY(self, x, y):
        self.pos[0] = x
        self.pos[1] = y

    def move(self, x, y):
        self.pos[0] += x
        self.pos[1] += y

    def getAbsoluteXY(self):
        if self.parent:
            return [self.pos[0] + self.parent.getAbsoluteXY()[0], self.pos[1] + self.parent.getAbsoluteXY()[1]]
        return [self.pos[0], self.pos[1]]

    def getFamily(self):
        family = [self]
        for child in self.children:
            family += child.getFamily()
        return family

    def update(self):
        for control in self.controls:
            control.update()
        for node in self.children:
            node.update()
