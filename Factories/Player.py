from Engine import Node
from Engine import AssetManager
from Controllers import PlayerAnim

class Player():
    def __init__(self):
        pass

    def makePlayer(self, color):
        player = Node.Node()
        player.attachControl(PlayerAnim.PlayerAnim(color))

        return player
        
