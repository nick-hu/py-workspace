#!/usr/bin/python

import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create socket
conn.bind(('localhost', 12345))  # Bind

while True:
    data, addr = conn.recvfrom(1024)  # Blocks
    # conn.recvfrom returns a tuple: ('data', ('ip', port))
    if data == 'quit':
        break
    print addr, '\n', data, '\n'

conn.close()
