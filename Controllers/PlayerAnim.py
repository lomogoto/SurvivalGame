from Engine import AssetManager
from pygame import transform

class PlayerAnim():
    def __init__(self, color):
        self.frame = 0
        self.down1 = AssetManager.load('Assets/Player/down.png')
        self.down2 = transform.flip(self.down1, True, False)

    def update(self):
        if self.frame%30 < 15:
            self.node.image = self.down1
        else:
            self.node.image = self.down2 
        self.frame += 1
