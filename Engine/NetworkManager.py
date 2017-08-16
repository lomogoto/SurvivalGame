import socket
import threading
import time

searchtime = 2

port = 3000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    udp.bind(('', port))
except:
    udp.bind(('', port+1))

running = False

def udpListener():
    print('Server Running')
    while running:
        newThread = threading.Thread(target = udpProcess, args = [udp.recvfrom(1024)])
        newThread.start()
    print('Server Stopped')

def udpProcess(data):
    message = data[0].decode()
    address = data[1]

    time.sleep(1)

    print(address)
    if message == 'getIP':
        udp.sendto('LOMOGOTO'.encode(), address)
        print('IP sent')

def getServers():
    udp.settimeout(1)
    udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    t0 = time.time()

    d = {}

    udp.sendto('getIP'.encode(), ('<broadcast>', port))
    while time.time() < t0 + searchtime:
        try:
            data = udp.recvfrom(1024)
            d[data[0].decode()] = data[1]
        except socket.timeout:
            pass

    udp.settimeout(None)

    print(d)

    return d

def joinServer(address):
    pass

def startServer():
    global running
    running = True
    udpThread = threading.Thread(target = udpListener)
    udpThread.start()

def closeSockets():
    global running
    if running:
        running = False
        try:
            udp.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass
        udp.close()
