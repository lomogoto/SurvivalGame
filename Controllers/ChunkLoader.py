from Factories import Chunk

class ChunkLoader():
    def __init__(self, followNode, saveFile):
        self.chunkFactory = Chunk.Chunk(0)
        self.chunks = {}
        self.follow = followNode

        self.chunkSize = 20

    def update(self):
        x, y = self.follow.getAbsoluteXY()
        x %= self.chunkSize
        y %= self.chunkSize

        newChunks = {}

        for i in range(-2,2):
            for j in range(-2,2):
                pos = (x + self.chunkSize*i, y + self.chunkSize*j)
                if str(pos) in self.chunks:
                    newChunks[str(pos)] = self.chunks[str(pos)]
                else:
                    newChunks[str(pos)] = self.chunkFactory.makeChunk(pos)
                    newChunks[str(pos)].setXY(pos[0], pos[1])

        for chunk in self.chunks:
            self.node.detach(self.chunks[chunk])

        self.chunks = newChunks
        for chunk in self.chunks:
            self.node.attach(self.chunks[chunk])
        
