#!/usr/bin/python

from time import sleep
import socket

UDP_IP = "10.6.66.10"
UDP_PORT = 1337

# wähle leiste
leiste = "\x02"

# black = hex(000000)
# white = hex(ffffff)
# blue = hex(0404d8)
# orange = hex(ffd400)

	s=1:15  # we have 15 LED strips
MESSAGE=leiste
for r in range(1,112):
	MESSAGE+="\xff\xff\xff"
while true: 
		# use HSL mode, create a simple sign wave on hue, fixed values for
        	#  saturation and luminance
		# hue sat lum
		# hsl = [0.5*(1+sin(2*pi*transp([1:N])/N + phi)) ones(N,1) 0.5*ones(N,1)]
		# rbg = hsl2rgb(hsl); # convert to RGB
	
 


	# send mesage
	sock = socket.socket(socket.AF_INET, # Internet
	socket.SOCK_DGRAM) # UDP
	sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))




# print "UDP target IP:", UDP_IP
# print "UDP target port:", UDP_PORT
# print "message:", MESSAGE

# endoffile
