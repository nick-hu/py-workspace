#!/usr/bin/python

import socket
from colorama import init

init()

port = raw_input('\n\033[30;1mBind to IP: ').split(':')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((port[0], int(port[1])))

print '\nListening for connection...'
sock.listen(1)
conn, addr = sock.accept()
print 'Connection accepted from\033[32;1m', addr[0] + ':' + str(addr[1]), '\n'

while True:
    data = conn.recv(1024).split('\n')
    if data[0] == 'quit':
        conn.close()
        break
    elif 'health' in data[0]:
        print '\n\n\033[31;1m' + data[0]
    elif 'started' in data[0]:
        print '\n\n\033[32;1m' + data[0]
    elif data[0].startswith('Student'):
        print '\n\n\033[32;1m' + data[0]
        print '\033[0m' + data[1] + '\nScore:\033[32;1m', data[2]
    else:
        data[0] = data[0].replace('<br>', '\n')
        print '\n\n\033[0mQuestion:\n\033[33;1m' + data[0]
        print '\033[0mStudent answer:\033[33;1m', data[1],
        colour = '[32;1m' if data[2] == 'Correct' else '[31;1m'
        print '\033' + colour + '--', data[2], '\n'
        print '\033[0mStudent stats: ', data[3]

raw_input('\n\n\033[0m(Connection ended; press return to exit)')
