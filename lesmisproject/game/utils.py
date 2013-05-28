#!/usr/bin/python

from colorama import init
from random import gauss

init()


def color(string, *c):
    '''String colouring with ANSI escape sequences.'''

    ansi = '\033['
    for code in c:
        if len(c) == 1:
            ansi = ansi + str(code)
        elif code == c[-1]:
            ansi = ansi + str(code)
        else:
            ansi = ansi + str(code) + ';'

    return (ansi + 'm%s' + '\033[0m') % string


def chance(val, sd):
    '''Normal distribution function to add element of luck.'''

    return int(gauss(val, sd))


scenes = {}
with open('scenes.txt') as sf:
    lines = [l.translate(None, '\n\r') for l in sf.readlines()]
    for l in range(0, len(lines), 7):  # Loop through scenarios
        oplines, ops = [lines[l+2], lines[l+3], lines[l+4], lines[l+5]], []
        for i in oplines:
            opline = i.split(': ')
            att, satt = opline[1].split(), [opline[1].split()[-1]]
            ops.append((opline[0], [int(x) for x in att[:-1]] + satt))
        scenes[lines[l]] = (lines[l+1], ops)

winscenes = {}
with open('winscenes.txt') as wsf:
    winlines = [l.translate(None, '\n\r') for l in wsf.readlines()]
    for l in range(0, len(winlines), 2):
        winscenes[winlines[l]] = winlines[l+1]
