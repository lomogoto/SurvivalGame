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
        self.layers = {}
        self.clip = 10

    #render a given node
    def renderNode(self, node):
        if node.image:
            #get the relative position to the camera
            c = self.getAbsoluteXY()
            n = node.getAbsoluteXY()
            rel = (n[0]-c[0], -(n[1]-c[1]))
            if abs(rel[0]) > self.clip or abs(rel[1]) > self.clip:
                return

            #convert to pixel location and center
            px = (rel[0]*self.unit[0], rel[1]*self.unit[1])
            centered = (px[0]+self.center[0]-self.unit[0]/2, px[1]+self.center[1]-(node.image.get_height()-self.unit[1]/2))
        
            #draw node
            self.scene.blit(node.image, centered)

    def renderOld(self):
        self.scene.fill((100,100,100))
        order = {}
        for node in self.parent.getFamily():
            index = (node.pos[2], -node.getAbsoluteXY()[1])
            if index in order:
                order[index].append(node)
            else:
                order[index] = [node]

        for key, nodeList in sorted(order.items()):
            for node in nodeList:
                self.renderNode(node)

    def makeNewLayer(self):
        AssetManager.box((self.w, self.h))
        return layer

    def draw(self, layer, image, pos):
        if image:
            #get the relative position to the camera
            c = self.getXY()
            rel = (pos[0]-c[0], -(pos[1]-c[1]))
            if abs(rel[0]) > self.clip or abs(rel[1]) > self.clip:
                return

            #convert to pixel location and center
            px = (rel[0]*self.unit[0], rel[1]*self.unit[1])
            centered = (px[0]+self.center[0]-self.unit[0]/2, px[1]+self.center[1]-(image.get_height()-self.unit[1]/2))
        
            #draw node
            self.layers[layer].blit(image, centered)

    def render(self, node = None, pos = (0, 0)):
        if node == None:
            self.layers = {}
            self.scene.fill((255,255,255))
            node = self.parent
        if not node.getDepth() in self.layers:
            self.layers[node.getDepth()] = AssetManager.box((self.w, self.h))
        pos = (pos[0]+node.getXY()[0], pos[1]+node.getXY()[1])
        self.draw(node.getDepth(), node.image, pos)
        for c in node.children:
            self.render(c, pos)
        for layer in sorted(self.layers):
            self.scene.blit(self.layers[layer], (0,0))
