import json
import socket

s = socket.socket()
s.connect(('localhost', 8000))
while True:
    data = json.loads(s.recv(1024).decode('utf-8'))
    print(data['file'])
    s.send(bytes(f'ack-{data["count"]}', 'utf-8'))
