import socket
from datetime import datetime


s = socket.socket()
s.bind(('localhost', 8000))
s.listen()

while True:
    conn, addr = s.accept()
    conn.send(bytes(str(datetime.now()), 'utf-8'))
