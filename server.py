import socket

s = socket.socket()
s.bind(('localhost', 8000))
s.listen()

while True:
    conn, addr = s.accept()
    conn.send(bytes("Hi! this is server here", "utf-8"))