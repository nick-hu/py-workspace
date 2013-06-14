#!/usr/bin/python

# SECRET:
# Mr. Arkiletian's mark-boosting function

def newmark(oldmark):
    return 10 * round(oldmark ** 0.5, 0)  # 10 times square root of old mark


while True:
    old = raw_input()
    if old == '':
        break
    print newmark(old), '\n'
