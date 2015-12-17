#!/usr/bin/python

import socket
from time import sleep

UDP_IP = "10.6.66.10"
UDP_PORT = 1337

# Farben:

weiss = "\xff\xff\xff"
rot = "\xf7\x29\x0e"
gelb = "\xfc\xf8\x05"
blau = "\x11\x05\xfc"

# CODE:

for i in range(1,10000):
	for l in range (1,16):
		leiste = l-1
		
		msg = ""
		msg2 = ""
		msg += chr(leiste)
		
		msg += (rot*2 + blau*2 + gelb*2) * (108/6)
		msg += rot*2 + blau*2 


		# send udp
		sock = socket.socket(socket.AF_INET, # Internet
		socket.SOCK_DGRAM) # UDP
		sock.sendto(msg, (UDP_IP, UDP_PORT))
	sleep(0.1)

