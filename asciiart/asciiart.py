#!/usr/bin/python

import Image
import sys

new = ['@', '#', 'A', '%', 'S', '<', '*', '+', ':', '.', ' ', ' ']
new2 = ['@', '*', '!', '-', ' ', ' ', ' ', ' ']
greyscale = new2
div = 256 // (len(greyscale) - 1)

img = Image.open(sys.argv[1]).convert('L')
if len(sys.argv) == 3:
    h = img.size[1]
else:
    h = int(sys.argv[3])
w = int(h * img.size[0] * 2.05 / img.size[1])
img = img.resize((w, h), Image.BICUBIC)

with open(sys.argv[2], 'w') as imgfile:
    for y in xrange(h):
        for x in xrange(w):
            lum = img.getpixel((x, y)) // div
            imgfile.write(greyscale[lum])
        imgfile.write('\n')
