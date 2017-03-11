import socket
import sys
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 11223
print "Binding Server to host:", host, ":: port:", port
s.bind((host,port))
print "Listening"
s.listen(5)
while True:
	c,addr = s.accept()
	t = time.time()
	print "Got Connection From Client at", addr
	while True:
		if time.time() - t >= 25:
			break
		rchar = c.recv(100).decode("ascii")
		if rchar:
			print rchar
