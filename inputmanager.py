import pygame

#class for input control
class InputManager():
    def __init__(self):
        self.poll()

        self.deadzone = 0.25

        self.listeners = {}
        self.keys = {pygame.K_ESCAPE : 'start',
                    pygame.K_q : 'back'}
        self.buttons = {0 : 'a',
                    1 : 'b',
                    2 : 'x',
                    3 : 'y',
                    7 : 'start'}
        self.axis = {0 : 'lx',
                    1 : 'ly'}

    def poll(self):
        pygame.joystick.quit()
        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()

    def update(self):
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN or e.type == pygame.KEYUP:
                state = e.type == pygame.KEYDOWN
                try:
                    for function in self.listeners[self.keys[e.key]]:
                        function(state)
                except KeyError:
                    pass

            elif e.type == pygame.JOYBUTTONDOWN or e.type == pygame.JOYBUTTONUP:
                state = e.type == pygame.JOYBUTTONDOWN
                try:
                    for function in self.listeners[self.buttons[e.button]]:
                        function(state)
                except KeyError:
                    pass 

            elif e.type == pygame.JOYAXISMOTION:
                state = e.value * (abs(e.value) > self.deadzone)
                try:
                    for function in self.listeners[self.axis[e.axis]]
                        function(state)
                except KeyError:
                    pass

    def register(self, inputName, function):
        if inputName in self.listeners:
            self.listeners[inputName].append(function)
        else:
            self.listeners[inputName] = [function]
