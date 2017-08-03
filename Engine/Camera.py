from Engine import Node

class Camera(Node.Node):
    def __init__(self, scene, unit = (1,1)):
        Node.Node.__init__(self)
        self.center = (scene.get_width()/2, scene.get_height()/2)
        self.unit = unit
        self.scene = scene

    #render a given node
    def renderNode(self, node):
        if node.image:
            #get the relative position to the camera
            c = self.getAbsoluteXY()
            n = node.getAbsoluteXY()
            rel = (n[0]-c[0], -(n[1]-c[1]))

            #convert to pixel location and center
            px = (rel[0]*self.unit[0], rel[1]*self.unit[1])
            centered = (px[0]+self.center[0]-self.unit[0]/2, px[1]+self.center[1]-(node.image.get_height()-self.unit[1]/2))
        
            #draw node
            self.scene.blit(node.image, centered)

    def render(self):
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
