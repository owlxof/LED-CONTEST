#!/usr/bin/python

import socket
from time import sleep

UDP_IP = "10.6.66.10"
UDP_PORT = 1337

# Farben:

weiss = "\xff\xff\xff"
blau = "\x0b\x58\xc4"

# CODE:

# for i in range(1,10000):
for l in range (1,16):
 	leiste = 3 
 	msg = ""
 	msg += chr(leiste)
 	msg += weiss * 112


	# send udp
 	sock = socket.socket(socket.AF_INET, # Internet
 	socket.SOCK_DGRAM) # UDP
 	sock.sendto(msg, (UDP_IP, UDP_PORT))
 	#sleep(0.1)

