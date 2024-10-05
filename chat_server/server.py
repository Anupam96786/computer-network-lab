import socket
import sys

s = socket.socket()
s.bind(('localhost', 8000))
s.listen()
conn, addr = s.accept()

while True:
    message = input("Me: ")
    if message == 'BYE':
        s.close()
        sys.exit()
    conn.send(bytes(message, 'utf-8'))
    print("Anupam: ", end='')
    print(conn.recv(1024).decode())
