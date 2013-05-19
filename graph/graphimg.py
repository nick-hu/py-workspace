#!/usr/bin/python

import Image
from func import *


def pixel(x, y):
    if y is None:
        return (None, None)
    center = (opt['width'] // 2, opt['height'] // 2)
    xstep = opt['width'] // (opt['xmax']-opt['xmin'])
    ystep = opt['height'] // (opt['ymax']-opt['ymin'])
    xpix = round(center[0] + xstep * x)
    ypix = round(center[1] + ystep * y)
    return (int(xpix), int(opt['height'] - ypix))

# Graph options
opt = {'xmin': -20, 'xmax': 20, 'ymin': -20, 'ymax': 20,
       'xscl': 1, 'yscl': 1, 'width': 400, 'height': 400,
       'axes': 3, 'point': 2, 'backg': 'white'}

while True:
    filename = raw_input('Write graph to file: ')
    while True:
        setting = raw_input('Change options: ')
        if setting.startswith('opt['):
            exec setting
            print 'Graph options updated: ', opt
        else:
            break

    graph = Image.new('RGB', (opt['width'], opt['height']), opt['backg'])
    gpix = graph.load()  # Create image and pixel access object

    while True:
        name = raw_input('\nFunction name: ')
        if name == '':
            break
        fn = raw_input('Function: ')
        colour = raw_input('Point color (r, g, b): ')
        exec name + ' = ' + fn
        exec 'colour = ' + colour

        pix = float(opt['xmax']-opt['xmin']) / float(opt['width'])

        for val in flrange(opt['xmin'], opt['xmax'] + pix, pix):
            exec 'yval = ' + name + '.val(' + str(val) + ')'

            coords, point = pixel(val, yval), []
            if coords[1] is not None:
                pl, pr = coords[0] - opt['point'] + 1, coords[0] + opt['point']
                pt, pb = coords[1] - opt['point'] + 1, coords[1] + opt['point']
                point.append(coords)
                for xc in xrange(pl, pr):
                    for yc in xrange(pt, pb):
                        point.append((xc, yc))

            for c in point:
                validx = 0 <= c[0] < opt['width']
                validy = 0 <= c[1] < opt['height']
                if validx and validy and coords[1] is not None:
                    gpix[c] = colour

        graph.save(filename)

    new = raw_input('\nNew graph [y/n]? ')
    if new == 'n':
        break
