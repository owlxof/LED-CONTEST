#!/usr/bin/python

import socket
from time import sleep

UDP_IP = "10.6.66.10"
UDP_PORT = 1337

# Farben:

schwarz = "\xff\xff\xff"

# CODE:

while True:
	for l in range (1,15):
		leiste = l-1
		msg = ""
		msg += chr(leiste)
		msg += schwarz * 112


		# send udp
		sock = socket.socket(socket.AF_INET, # Internet
		socket.SOCK_DGRAM) # UDP
		sock.sendto(msg, (UDP_IP, UDP_PORT))


