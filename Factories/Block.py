from Engine import Node
from Engine import AssetManager

class Block():
    def __init__(self):
        pass

    def makeBlock(self, name):
        block = Node.Node()

        if name == 'grass':
            block.image = AssetManager.load('Assets/Blocks/grass.png')
        elif name == 'water':
            block.image = AssetManager.load('Assets/Blocks/grass.png')
        block.setDepth(-1)

        return block
