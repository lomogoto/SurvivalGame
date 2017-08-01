class Graph():
    def __init__(self, camera):
        self.camera = camera
        self.children = []

    def attachChild(self, child):
        self.children.append(child)

    def removeChild(self, child):
        self.children.remove(child)

    def getChildren(self):
        return self.children

    def getCamera(self):
        return self.camera

    #render the nodes using the set camera
    def render(self):
        #dictionary to render in the proper order
        order = {}

        #render things of the same depth and y position at the same time
        for node in self.children:
            #sort by depth first, then y position
            index = (node.pos[2], node.pos[1])

            #add node to correct list or make a new list
            if index in order:
                order[index].append(node)
            else:
                order[index] = [node]

        #sorted returns a list of tupples in order to loop over
        for key, nodeList in sorted(order.items()):
            for node in nodeList:
                sel.camera.render(node)
