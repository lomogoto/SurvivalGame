import pygame

deadzone = 0.25

listeners = {}

keys = {pygame.K_ESCAPE : 'start',
        pygame.K_q : 'back',
        pygame.K_UP : 'up',
        pygame.K_DOWN : 'down',
        pygame.K_RETURN : 'a'}
buttons = {0 : 'a',
        1 : 'b',
        2 : 'x',
        3 : 'y',
        7 : 'start'}
axis = {0 : ('left', 'right'),
        1 : ('up', 'down')}
axisState = {0:0, 1:0}

joystick = None

def poll():
    pygame.joystick.quit()
    pygame.joystick.init()
    global joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

def update():
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN or e.type == pygame.KEYUP:
            value = e.type == pygame.KEYDOWN
            try:
                for function in listeners[keys[e.key]]:
                    function(value)
            except KeyError:
                pass

        elif e.type == pygame.JOYBUTTONDOWN or e.type == pygame.JOYBUTTONUP:
            value = e.type == pygame.JOYBUTTONDOWN
            try:
                for function in listeners[buttons[e.button]]:
                    function(value)
            except KeyError:
                pass 

        elif e.type == pygame.JOYAXISMOTION:
            value = (e.value > deadzone) - (e.value < -deadzone)
            try:
                if not value == axisState[e.axis]:
                    axisState[e.axis] = value
                    for function in listeners[axis[e.axis][value > 0]]:
                        function(abs(value))
                    for function in listeners[axis[e.axis][value <= 0]]:
                        function(0)
            except KeyError:
                pass

def register(inputName, function):
    if inputName in listeners:
        listeners[inputName].append(function)
    else:
        listeners[inputName] = [function]

def release(inputName, function):
    listeners[inputName].remove(function)
