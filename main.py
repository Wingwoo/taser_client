from gpiozero import LED
from time import sleep

taser = LED(17)

import socket

def tase(time):
    print("Tasing for " + str(time) +  "ms")
    taser.on()
    sleep(time / 1000)
    taser.off()
    print("Taser deactivated")

host = "10.0.0.6"
port = 1337
bsize = 8

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print("Connected")
except:
    print("Connection failed")
    exit()

while True:
    data = s.recv(bsize)
    if data != "":
        ms = int(data.decode())
        tase(ms)
    sleep(0.1)

