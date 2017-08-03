from Engine import Node
from Engine import AssetManager

class Button():
    def __init__(self):
        pass

    def makeButton(self, title, function, args = []):
        button = Node.Node()
        button.setTag('name', title)
        button.setTag('function', function)
        button.setTag('args', args)
        button.image = AssetManager.text('Assets/font.png', title)

        return button
