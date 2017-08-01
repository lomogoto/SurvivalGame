import node

class Camera(node.Node):
    def __init__(self, scene, unit = (1,1)):
        node.Node.__init__()
        self.center = (scene.get_width()/2, scene.get_height()/2)
        self.unit = unit
        self.scene = scene

    #render a given node
    def renderNode(self, node):
        #get the relative position to the camera
        rel = (node.pos[0]-self.pos[0], node.pos[1]-self.pos[1])

        #convert to pixel location and center
        pxPos = (relPos[0]*self.unit[0], relPos[1]*self.unit[1])
        centeredPos = (pxPos[0]+self.center[0], pxPos[1]+self.center[1])
        
        #draw node
        self.scene.blit(node.getImage(), centeredPos)

    def render(self):
        order = {}
        for node in self.parent.getFamily():
            index = (node.pos[2], node.pos[1])
            if index in order:
                order[index].append(node)
            else:
                order[index] = [node]

        for key, nodeList in sorted(order.items()):
            for node in nodeList:
                renderNode(node)
