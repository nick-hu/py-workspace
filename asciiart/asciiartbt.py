#!/usr/bin/python

import Image
import sys

img = Image.open(sys.argv[1]).convert('L')
if len(sys.argv) == 3:
    h = img.size[1]
else:
    h = int(sys.argv[3])

text = ""
if len(sys.argv) >= 5:
    with open(sys.argv[4]) as source:
        text = source.read().translate(None, "\n\r ")
if not text:
    text = "l"
char_count, tlen, threshold = 0, len(text), 55

w = int(h * img.size[0] * 2.05 / img.size[1])
img = img.resize((w, h), Image.BICUBIC)

with open(sys.argv[2], 'w') as imgfile:
    for y in xrange(h):
        for x in xrange(w):
            if img.getpixel((x, y)) < threshold:
                char = text[char_count % tlen]
                char_count += 1
                imgfile.write(char)
            else:
                imgfile.write(" ")
        imgfile.write('\n')
