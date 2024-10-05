import socket

s = socket.socket()
s.connect(('localhost', 8000))

while True:
    print("Server: ", end='')
    print(s.recv(1024).decode())
    s.send(bytes(input("Me: "), 'utf-8'))
