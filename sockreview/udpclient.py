#!/usr/bin/python

import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Uses ephemeral port: random, unused port

while True:
    data = raw_input('\nSend: ')
    conn.sendto(data, ('localhost', 12345))  # Send to localhost, port
    if data == 'quit':
        break

conn.close()
