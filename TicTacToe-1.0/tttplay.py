#!/usr/bin/python
# TIC-TAC-TOE PLAYING MODULE

import random
import string
import time


def gengrid(grid):  # Grid generation and grid codes
    print '''
              a   b   c
            =============
        1   | ''' + grid[0] + ' | ' + grid[1] + ' | ' + grid[2] + ''' |
            =============
        2   | ''' + grid[3] + ' | ' + grid[4] + ' | ' + grid[5] + ''' |
            =============
        3   | ''' + grid[6] + ' | ' + grid[7] + ' | ' + grid[8] + ''' |
            =============
            '''


def genstats():
    with open('stats.txt') as s:
        stat = s.readlines()[-1].split()
    print 'Tic-Tac-Toe Stats as of:', ' '.join(stat[3::])
    print 'Wins:', stat[0], '| Losses:', stat[1], '| Ties:', stat[2]


def play1(grid):  # Beginner algorithm: picks random empty square
    while True:
        ch = random.randrange(0, 9)
        if grid[ch] == 'X' or grid[ch] == 'O':
            continue
        break

    grid[ch] = 'O'
    print 'Python\'s move:'


def play2(grid):  # Intermediate algorithm: reactionary
    global rowcode, react

    ch, xawin = 'x', ['X', 'X']

    for pair in react:
        if (grid[pair[0]] == grid[pair[1]] == 'X' or
           grid[pair[0]] == grid[pair[1]] == 'O'):
            ch = react[pair]
            if grid[ch] == 'X' or grid[ch] == 'O':
                ch = 'x'
                continue
            break

    if ch == 'x':
        while True:
            ch = random.randrange(0, 9)
            if grid[ch] == 'X' or grid[ch] == 'O':
                continue
            break

    grid[ch] = 'O'
    print 'Python\'s move:'


def chkwin(grid):  # Checks for win/loss/tie
    global name, rowcode
    win = ''

    for x in range(len(rowcode)):
        if (grid[rowcode[x][0]] == grid[rowcode[x][1]] ==
           grid[rowcode[x][2]] == 'X'):
            win = 'X'
            break
        elif (grid[rowcode[x][0]] == grid[rowcode[x][1]] ==
              grid[rowcode[x][2]] == 'O'):
            win = 'O'
            break

    if ' ' not in grid and win == '':
        win = 't'

    if win == 'X':
        return 'v'
    elif win == 'O':
        return '\nDEFEAT! Python wins!'
    elif win == 't':
        return '\nTIE! Nobody wins!'


def chkstat(grid):
    global w, l, t

    if chkwin(grid) == 'v':
        w = w+1
    elif chkwin(grid) == '\nDEFEAT! Python wins!':
        l = l+1
    else:
        t = t+1


def stat():
    global w, l, t

    with open('stats.txt', 'r+') as s:
        stat = s.readlines()[-1].split()[0:3]
        stat[0] = str(int(stat[0])+w)
        stat[1] = str(int(stat[1])+l)
        stat[2] = str(int(stat[2])+t)

        s.write('\n'+str(' '.join(stat))+' '+time.asctime())

# Winning grid codes for chkwin function
rowcode = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
           (0, 3, 6), (1, 4, 7), (2, 5, 8),
           (0, 4, 8), (2, 4, 6))

# Codes to react to for play2 function
react = {(0, 1): 2, (1, 2): 0, (0, 2): 1,
         (3, 4): 5, (4, 5): 3, (3, 5): 4,
         (6, 7): 8, (7, 8): 6, (6, 8): 7,
         (0, 3): 6, (3, 6): 0, (0, 6): 3,
         (1, 4): 7, (4, 7): 1, (1, 7): 4,
         (2, 5): 8, (5, 8): 2, (2, 8): 5,
         (0, 4): 8, (4, 8): 0, (0, 8): 4,
         (2, 4): 6, (4, 6): 2, (2, 6): 4}

w, l, t = 0, 0, 0
