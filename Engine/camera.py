from Engine import node

class Camera(node.Node):
    def __init__(self, scene, unit = (1,1)):
        node.Node.__init__(self)
        self.center = (scene.get_width()/2, scene.get_height()/2)
        self.unit = unit
        self.scene = scene

    #render a given node
    def renderNode(self, node):
        #get the relative position to the camera
        c = self.getAbsoluteXY()
        n = node.getAbsoluteXY()
        rel = (n[0]-c[0], n[1]-c[1])

        #convert to pixel location and center
        px = (rel[0]*self.unit[0], rel[1]*self.unit[1])
        centered = (px[0]+self.center[0], px[1]+self.center[1])
        
        #draw node
        if node.image:
            self.scene.blit(node.image, centered)

    def render(self):
        self.scene.fill((0,0,0))
        order = {}
        for node in self.parent.getFamily():
            index = (node.pos[2], node.getAbsoluteXY()[1])
            if index in order:
                order[index].append(node)
            else:
                order[index] = [node]

        for key, nodeList in sorted(order.items()):
            for node in nodeList:
                self.renderNode(node)
