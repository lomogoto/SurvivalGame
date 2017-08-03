from Engine import InputManager

class MenuNav():
    def __init__(self, cursor, buttons):
        self.selected = 0
        self.cursor = cursor
        self.buttons = buttons

        InputManager.register('up', self.moveUp)
        InputManager.register('down', self.moveDown)
        InputManager.register('a', self.select)

    def update(self):
        self.buttons[self.selected].attach(self.cursor)

    def moveUp(self, value):
        if value > 0 and self.selected > 0:
            self.selected -= 1

    def moveDown(self, value):
        if value > 0 and self.selected < len(self.buttons)-1 :
            self.selected += 1

    def select(self, value):
        if value:
            InputManager.release('up', self.moveUp)
            InputManager.release('down', self.moveDown)
            InputManager.release('a', self.select)

            parent = self.node.getParent()
            parent.detach(self.node)

            args = self.buttons[self.selected].getTag('args')

            if args == []:
                parent.attach(self.buttons[self.selected].getTag('function')())
            else:
                parent.attach(self.buttons[self.selected].getTag('function')(args))
