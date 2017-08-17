from Engine import Node
from Engine import AssetManager

class Camera(Node.Node):
    def __init__(self, scene, unit = (1,1)):
        Node.Node.__init__(self)
        self.center = (scene.get_width()/2, scene.get_height()/2)
        self.unit = unit
        self.scene = scene
        self.w = scene.get_width()
        self.h = scene.get_height()
        self.queue = {}
        self.clip = 10

    def draw(self, image, pos):
        px = (pos[2]*self.unit[0], -pos[1]*self.unit[1])
        centered = (px[0]+self.center[0]-self.unit[0]/2, px[1]+self.center[1]-(image.get_height()-self.unit[1]/2))
        
        self.scene.blit(image, centered)

    def render(self):
        self.queue = {}
        self.scene.fill((100,100,100))

        self.queueNodes(self.getParent())

        for pos in sorted(self.queue):
            for image in self.queue[pos]:
                self.draw(image, pos)

    def queueNodes(self, node, pos = (0,0,0)):
        pos = (node.getDepth(), pos[1]+node.getY(), pos[2]+node.getX())
        rel = (pos[0], pos[1]-self.getY(), (pos[2]-self.getX()))
        if abs(rel[1]) > self.clip or abs(rel[2]) > self.clip or node.getImage() == None:
            pass
        elif not rel in self.queue:
            self.queue[rel] = [node.getImage()]
        else:
            self.queue[rel].append(node.getImage())

        for child in node.getChildren():
            self.queueNodes(child, pos)
