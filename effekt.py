#!/usr/bin/python

import socket
from time import sleep
import colorsys

# definiere UDP-Ziel:
UDP_IP = "10.6.66.10"
UDP_PORT = 1337

# hier evtl eine liste mit unterschiedlichen farben oder farbeffekte
# einbauen


# Farben:
weiss = "\xff\xff\xff"
blau = "\x0b\x58\xc4"



# für jede Leiste ein Packet, für jede LED 3 bytes (112 LEDs)

# for i in range(1,10000000):
for l in range (1,16): # über leisten iterieren
 	leiste = l-1
	msg = ""
 	msg += chr(leiste)
 	for led in range (1,112): #über leds iterieren
	msg += blau * 112


	# send udp packet
 	sock = socket.socket(socket.AF_INET, # Internet
 	socket.SOCK_DGRAM) # UDP
 	sock.sendto(msg, (UDP_IP, UDP_PORT))
 	# sleep(0.1)
# endoffile
