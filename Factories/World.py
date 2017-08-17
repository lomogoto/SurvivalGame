from Engine import Node
from Controllers import ChunkLoader
from Factories import Player

class World():
    def __init__(self):
        self.playerFactory = Player.Player()
        pass

    def makeWorld(self, seed):
        world = Node.Node()
        player = self.playerFactory.makePlayer(None)
        chunkController = ChunkLoader.ChunkLoader(player, {})
        world.attach(player)
        world.attachControl(chunkController)

        return world
