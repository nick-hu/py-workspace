#!/usr/bin/env python

import Image
from sys import argv


def colour_delta(ref, rgb):
    return sum(map(lambda p: (p[1] - p[0])**2, zip(ref, rgb))) ** 0.5

bounds = [map(int, raw_input("x-bounds: ").split()),
          map(int, raw_input("y-bounds: ").split())]
selected = {}
while True:
    data = map(int, raw_input("Reference colour / threshold: ").split())
    if not data:
        break
    selected[tuple(data[:-1])] = data[-1]

old_img = Image.open(argv[1]).convert('RGB')
old_pix = old_img.load()
new_img = old_img.copy().convert('L').convert('RGB')
new_pix = new_img.load()

if not bounds[0]:
    bounds[0] = [0, old_img.size[0]]
if not bounds[1]:
    bounds[1] = [0, old_img.size[1]]

for x in xrange(*bounds[0]):
    for y in xrange(*bounds[1]):
        coloured = old_pix[x, y]
        for scolor in selected:
            if colour_delta(scolor, coloured) < selected[scolor]:
                new_pix[x, y] = coloured

new_img.save("{}_new.{}".format(*argv[1].split('.')))
