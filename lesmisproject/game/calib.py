#!/usr/bin/python

from colorama import init

init()

print '\033[2J'
print '+' + '-' * 78 + '+'
print '''| TERMINAL WINDOW CALIBRATION
|
| Recommended size: 80x24
|
| Ensure that you can see all corners of this box properly and
| all the colours display correctly.
|'''
print '''| \033[31mRed\033[0m \t\t\033[41mRed background\033[0m
| \033[32mGreen\033[0m \t\033[42mGreen background\033[0m
| \033[33mYellow\033[0m \t\033[43mYellow background\033[0m
| \033[34mBlue\033[0m \t\t\033[44mBlue background\033[0m
| \033[35mMagenta\033[0m \t\033[45mMagenta background\033[0m
| \033[36mCyan\033[0m \t\t\033[46mCyan background\033[0m
| \033[37mWhite\033[0m \t\033[47;30mWhite background\033[0m
| \033[31;1mBright Red\033[0m
| \033[32;1mBright Green\033[0m
| \033[33;1mBright Yellow\033[0m
| \033[34;1mBright Blue\033[0m
| \033[35;1mBright Magenta\033[0m
| \033[36;1mBright Cyan\033[0m
| \033[37;1mBright White\033[0m'''

stall = raw_input('+' + '-' * 78)
