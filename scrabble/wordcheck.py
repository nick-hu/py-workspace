#!/usr/bin/python

print 'Scrabble word checker (TWL2)'

with open('owl.txt') as f:
    twlist = f.read().split()

while True:
    word = raw_input('\nWord to check: ')
    if word == '':
        break
    if word.upper() in twlist:
        print word.upper(), 'is a VALID word in the TWL'
    else:
        print word.upper(), 'is INVALID'
