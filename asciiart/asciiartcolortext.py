#!/usr/bin/python

import Image
import sys

img = Image.open(sys.argv[1])
img = img.convert('P', palette=Image.ADAPTIVE, colors=256)
if len(sys.argv) == 3:
    h = img.size[1]
else:
    h = int(sys.argv[3])
w = int(h * img.size[0] * 2 / img.size[1])
img = img.resize((w, h), Image.BICUBIC)

palimg = img.copy().resize((256, 1))  # Figure out image palette
palimg.putdata(xrange(256))
palimg = palimg.convert('RGB')  # Obtain RGB values
pal = [palimg.getpixel((x, 0)) for x in xrange(256)]

text = ""
if len(sys.argv) >= 5:
    with open(sys.argv[4]) as source:
        text = source.read().translate(None, "\n\r ")
if not text:
    text = "l"
char_count, tlen = 0, len(text)

with open(sys.argv[2], 'w') as ifile:  # Write RTF code
    ifile.write(r'{\rtf1\ansi\ansicpg1252\deff0\deflang4105' + '\n')
    ifile.write(r'{\fonttbl{\f0\fnil\fcharset0 DejaVu Sans Mono;}}' + '\n')
    ifile.write(r'{\colortbl ;')
    for color in pal:
        r, g, b = str(color[0]), str(color[1]), str(color[2])
        ifile.write(r'\red' + r + r'\green' + g + r'\blue' + b + ';')

    ifile.write('}\n{\*\generator Nicholas\' ASCII art program;}')
    ifile.write(r'\viewkind4\uc1\pard\sl240\slmult1\lang9\f0\fs2' + '\n')

    for y in xrange(h):
        for x in xrange(w):
            char = text[char_count % tlen]
            char_count += 1
            ifile.write('\cf' + str(img.getpixel((x, y)) + 1) + ' ' + char)
        ifile.write('\par' + '\n')
    ifile.write('}')
