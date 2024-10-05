import socket

s = socket.socket()
s.connect(('localhost', 8000))
s.send(bytes("Hi! this is client here", "utf-8"))
print(s.recv(1024))