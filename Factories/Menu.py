from Engine import Node
from Engine import AssetManager
from Engine import InputManager
from Engine import FileManager
from Engine import NetworkManager
from Factories import Button
from Controllers import MenuNav

class Menu():
    def __init__(self, quitFunction):
        self.buttonFactory = Button.Button()
        self.quit = quitFunction
        self.settings = FileManager.load('Data/settings.json.gz')

    def makeMenu(self, title, buttonList):
        menu = Node.Node()

        text = Node.Node()
        text.image = AssetManager.text('Assets/GUI/font.png', title)
        text.setXY(-9,6)
        menu.attach(text)

        cursor = Node.Node()
        cursor.image = AssetManager.load('Assets/GUI/cursor.png')
        cursor.setXY(-1, 0)
        text.attach(cursor)

        buttons = []

        for args in buttonList:
            try:
                buttons.append(self.buttonFactory.makeButton(args[0], args[1], args[2]))
            except:
                buttons.append(self.buttonFactory.makeButton(args[0], args[1]))

        rank = 0
        for button in buttons:
            button.setXY(1, -2 - rank)
            text.attach(button)
            rank += 1

        nav = MenuNav.MenuNav(cursor, buttons)
        menu.attachControl(nav)

        return menu

    def makeMainMenu(self):
        NetworkManager.closeSockets()
        buttonList = (('PLAY', self.makePlayMenu),
                ('JOIN', self.makeJoinMenu),
                ('CHARACTER', self.makeCharacterMenu),
                ('SETTINGS', self.makeSettingsMenu),
                ('QUIT', self.quit))
        return self.makeMenu('MAIN MENU', buttonList)

    def makePlayMenu(self):
        NetworkManager.startServer()
        buttonList = (('START', self.makeMainMenu),
                ('BACK', self.makeMainMenu))
        return self.makeMenu('PLAY', buttonList)

    def makeJoinMenu(self):
        servers = NetworkManager.getServers()
        buttonList = [('REFRESH', self.makeJoinMenu)]
        for server in servers:
            buttonList.append((server, self.joinServer, servers[server]))
        buttonList.append(('BACK', self.makeMainMenu))
        return self.makeMenu('JOIN', buttonList)

    def makeCharacterMenu(self):
        FileManager.save('Data/settings.json.gz')
        buttonList = (('COLOR', self.makeColorMenu),
                ('BACK', self.makeMainMenu))
        return self.makeMenu('CHARACTER', buttonList)

    def makeSettingsMenu(self):
        FileManager.save('Data/settings.json.gz')
        buttonList = (('RESOLUTION', self.makeResolutionMenu),
                ('POLL', self.poll),
                ('BACK', self.makeMainMenu))
        return self.makeMenu('SETTINGS', buttonList)

    def makeResolutionMenu(self):
        buttonList = (('FULLSCREEN', self.setResolution, [0, 0]),
                ('1920 X 1080', self.setResolution, [1920, 1080]),
                ('1600 X 900', self.setResolution, [1600, 900]),
                ('1280 X 720', self.setResolution, [1280, 720]),
                (' 960 X 540', self.setResolution, [960, 540]),
                ('BACK', self.makeSettingsMenu))
        return self.makeMenu('RESOLUTION', buttonList)

    def makeColorMenu(self):
        buttonList = (('RED', self.setColor, [200, 0, 0]),
                ('YELLOW', self.setColor, [100, 100, 0]),
                ('GREEN', self.setColor, [0, 200, 0]),
                ('CYAN', self.setColor, [0, 100, 100]),
                ('BLUE', self.setColor, [0, 0, 200]),
                ('MAGENTA', self.setColor, [100, 0, 100]),
                ('BACK', self.makeCharacterMenu))
        return self.makeMenu('COLOR', buttonList)

    def joinServer(self, address):
        print(address)
        return self.makeMainMenu()

    def setResolution(self, args):
        self.settings['dimentions'] = args
        return self.makeSettingsMenu()

    def setColor(self, args):
        self.settings['color'] = args
        return self.makeCharacterMenu()

    def poll(self):
        InputManager.poll()
        return self.makeSettingsMenu()
