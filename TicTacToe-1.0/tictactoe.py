#!/usr/bin/python
# PYTHON TIC-TAC-TOE PLAYER 1.0

import tttplay

print '\t ====== PYTHON TIC-TAC-TOE PLAYER ====== \n'

name = raw_input('Please enter your name: ')
print '\nWelcome,', name + '!\n'
tttplay.genstats()

while True:
    grid = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    diff = int(raw_input('\nDifficulty level (1-3): '))
    tttplay.gengrid(grid)

    while True:
        while True:
            xposraw = raw_input('Your move: ')
            rawconv = {'a1': 0, 'b1': 1, 'c1': 2,
                       'a2': 3, 'b2': 4, 'c2': 5,
                       'a3': 6, 'b3': 7, 'c3': 8}
            if xposraw not in rawconv:
                print '\nError: Invalid position; enter in format "a1"\n'
                continue
            xpos = rawconv[xposraw]
            if grid[xpos] == 'X' or grid[xpos] == 'O':
                print '\nError: Invalid move\n'
                continue
            break
        grid[xpos] = 'X'

        tttplay.gengrid(grid)

        if tttplay.chkwin(grid) is not None:
            if tttplay.chkwin(grid) == 'v':
                print '\nVICTORY!', name, 'wins!'
            else:
                print tttplay.chkwin(grid)
            break

        elif diff == 1:
            tttplay.play1(grid)
            tttplay.gengrid(grid)
            if tttplay.chkwin(grid) is not None:
                if tttplay.chkwin(grid) == 'v':
                    print '\nVICTORY!', name, 'wins!'
                else:
                    print tttplay.chkwin(grid)
                break

        elif diff == 2:
            tttplay.play2(grid)
            tttplay.gengrid(grid)
            if tttplay.chkwin(grid) is not None:
                if tttplay.chkwin(grid) == 'v':
                    print '\nVICTORY!', name, 'wins!'
                else:
                    print tttplay.chkwin(grid)
                break

        elif diff == 3:
            print 'Difficulty level 3 coming soon!'

    tttplay.chkstat(grid)
    cont = raw_input('\nPlay again? (Yes[y]/No[n]): ')
    if cont == 'y':
        continue
    print '\n'
    break

tttplay.stat()
tttplay.genstats()

print '\nGoodbye,', name + '!'
