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



msg = ""
for i in range(256):
	msg += chr(255-i) + chr(i) + chr(0)
for i in range(256):
	msg += chr(0) + chr(255-i) + chr(i)
for i in range(256):
	msg += chr(i) + chr(0) + chr(255-i)

msg = msg*19
#print "".join("{:02x}".format(ord(c)) for c in msg)


for i in range(1,10000):
		# send udp
	sock = socket.socket(socket.AF_INET, # Internet
	socket.SOCK_DGRAM) # UDP
	sock.sendto(chr(3) + msg[0:336][::-1], (UDP_IP, UDP_PORT))
	sock.sendto(chr(1) + msg[336:2*336][::-1], (UDP_IP, UDP_PORT))
	sock.sendto(chr(4) + msg[2*336:3*336][::-1], (UDP_IP, UDP_PORT))
	sock.sendto(chr(0) + msg[3*336:4*336], (UDP_IP, UDP_PORT))
	sock.sendto(chr(14) + msg[4*336:5*336][::-1], (UDP_IP, UDP_PORT))
	sock.sendto(chr(9) + msg[5*336:6*336][::-1], (UDP_IP, UDP_PORT))
	sock.sendto(chr(12) + msg[6*336:7*336][::-1], (UDP_IP, UDP_PORT))
	sock.sendto(chr(10) + msg[7*336:8*336], (UDP_IP, UDP_PORT))
	sock.sendto(chr(2) + msg[8*336:9*336][::-1], (UDP_IP, UDP_PORT))
	sock.sendto(chr(5) + msg[9*336:10*336], (UDP_IP, UDP_PORT))
	sock.sendto(chr(6) + msg[10*336:11*336], (UDP_IP, UDP_PORT))
	sock.sendto(chr(11) + msg[11*336:12*336], (UDP_IP, UDP_PORT))
	sock.sendto(chr(13) + msg[12*336:13*336][::-1], (UDP_IP, UDP_PORT))
	sock.sendto(chr(7) + msg[13*336:14*336], (UDP_IP, UDP_PORT))
	sock.sendto(chr(8) + msg[14*336:15*336], (UDP_IP, UDP_PORT))
	sleep(0.1)

#for i in range(1,10000):
#		# send udp
#	sock = socket.socket(socket.AF_INET, # Internet
#	socket.SOCK_DGRAM) # UDP
#	sock.sendto(chr(3) + rot*336, (UDP_IP, UDP_PORT))
#	sock.sendto(chr(1) + rot*336, (UDP_IP, UDP_PORT))
#	sock.sendto(chr(4) + rot*336, (UDP_IP, UDP_PORT))
#	sock.sendto(chr(0) + rot*336, (UDP_IP, UDP_PORT))
#	sock.sendto(chr(14) +rot*336, (UDP_IP, UDP_PORT))
#	sock.sendto(chr(9) + rot*336, (UDP_IP, UDP_PORT))
#	sock.sendto(chr(12) +rot*336, (UDP_IP, UDP_PORT))
#	sock.sendto(chr(10) +rot*336, (UDP_IP, UDP_PORT))
#	sock.sendto(chr(2) + rot*336, (UDP_IP, UDP_PORT))
#	sock.sendto(chr(5) + rot*336, (UDP_IP, UDP_PORT))
#	sock.sendto(chr(6) + rot*336, (UDP_IP, UDP_PORT))
#	sock.sendto(chr(11) +rot*336, (UDP_IP, UDP_PORT))
#	sock.sendto(chr(13) +rot*336, (UDP_IP, UDP_PORT))
#	sock.sendto(chr(7) + rot*336, (UDP_IP, UDP_PORT))
#	sock.sendto(chr(8) + rot*336, (UDP_IP, UDP_PORT))
#	sleep(0.1)

