import socket

s = socket.socket()
s.connect(('localhost', 8000))

data = s.recv(1024)
print(data)
