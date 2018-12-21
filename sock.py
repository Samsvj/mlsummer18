#!usr/bin/env python2

import socket

#sender side of socket..

s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


s.bind(("127.0.0.1",1555))

msg=raw_input("type anything...!!!!!")


s.sendto(msg,("127.0.0.1",1234))
'''
while True:
	s.recvfrom(100)

'''
