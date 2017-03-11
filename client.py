import socket
from time import sleep

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 11223
print "Connecting to", host, "at port", port
s.connect((host,port))
while True:
	x = #get the key
	s.sendall(x.encode())

