import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 11223
print "Binding Server to host:", host, ":: port:", port
s.bind((host,port))
print "Listening"
s.listen(5)
while True:
	c,addr = s.accept()
	print "Got Connection From Client at", addr
	while True:
		rchar = s.recv(100).decode("ascii")
		if rchar:
			print rchar

