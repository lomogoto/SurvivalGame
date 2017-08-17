from Engine import Node
from Factories import Block

class Chunk():
    def __init__(self, seed):
        self.blockFactory = Block.Block()
        self.seed = seed

    def getBlockName(self, x, y):
        if abs(x) < 10 and abs(y) < 10:
            return 'grass'
        else:
            return 'water'

    def makeChunk(self, pos):
        chunk = Node.Node()

        for i in range(20):
            for j in range(20):
                block = self.blockFactory.makeBlock(self.getBlockName(pos[0] + i, pos[1] + j))
                block.setXY(i,j)
                chunk.attach(block)

        return chunk
