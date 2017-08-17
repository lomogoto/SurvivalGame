#class for all game nodes
class Node():
    def __init__(self):
        self.pos = [0, 0, 0]
        self.controls = []
        self.image = None
        self.parent = None
        self.children = []
        self.tags = {}

    def attach(self, child):
        if child.parent:
            child.parent.detach(child)
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

    def hasControl(self, controlType):
        return any(isinstance(control, controlType) for control in self.controls)

    def getChildren(self):
        return self.children
    def getParent(self):
        return self.parent

    def setImage(self, image):
        self.image = image
    def getImage(self):
        return self.image

    def setX(self, x):
        self.pos[2] = x
    def getX(self):
        return self.pos[2]

    def setY(self, y):
        self.pos[1] = y
    def getY(self):
        return self.pos[1]

    def setDepth(self, z):
        self.pos[0] = z
    def getDepth(self):
        return self.pos[0]

    def setTag(self, name, value):
        self.tags[name] = value
    def getTag(self, name):
        return self.tags[name]

    def update(self):
        for control in self.controls:
            control.update()
        for node in self.children:
            node.update()
