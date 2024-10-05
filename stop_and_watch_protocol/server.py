import json
import socket
from time import sleep

s = socket.socket()
s.bind(('localhost', 8000))
s.listen()

count = 0

conn, addr = s.accept()

while True:
    conn.send(bytes(json.dumps({'file': f"File {count} sent...", 'count': count}), 'utf-8'))
    if conn.recv(1024).decode('utf-8') == f"ack-{count}":
        print(f"File {count} sent without any error")
    sleep(1)
    count += 1
