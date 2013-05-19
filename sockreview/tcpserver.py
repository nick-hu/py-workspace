#!/usr/bin/python

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow reuse
sock.bind(('localhost', 12345))

sock.listen(1)  # Listen for 1 connection
conn, addr = sock.accept()
# Accept connection and get conn object and address tuple
print addr

while True:
    data = conn.recv(1024)
    if data == 'quit':
        break
    print data

conn.close()
