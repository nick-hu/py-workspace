#!/usr/bin/python

import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(('localhost', 12345))  # Connect

while True:
    data = raw_input('\nSend: ')
    conn.send(data)
    if data == 'quit':
        break

conn.close()
