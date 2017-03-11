import socket

s = socket.socket()
host = socket.gethostname()
port = 11223
s.bind((host,port))

s.listen(5)
while True:
	c,addr = s.accept()
	print "Got Connection From Client at ", addr
	while True:
		rchar = s.recv(1);
		if rchar:
			print rchar

