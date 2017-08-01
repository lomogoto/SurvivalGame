class Camera():
    def __init__(self, scene, unit = (1,1)):
        self.pos = [0, 0]
        self.center = (scene.w/2, scene.h/2)
        self.unit = unit
        self.scene = scene

    #render a given node
    def render(self, node):
        #get the relative position to the camera
        rel = (node.pos[0]-self.pos[0], node.pos[1]-self.pos[1])

        #convert to pixel location and center
        pxPos = (relPos[0]*self.unit[0], relPos[1]*self.unit[1])
        centeredPos = (pxPos[0]+self.center[0], pxPos[1]+self.center[1])
        
        #draw node
        self.scene.blit(node.getImage(), centered pos)
