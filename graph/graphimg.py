#!/usr/bin/python

from math import *
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

# Graph options (defaults)
opt = {'xmin': -20, 'xmax': 20, 'ymin': -20, 'ymax': 20,
       'width': 1000, 'height': 1000, 'xscl': 1, 'yscl': 1,
       'axes': 2, 'drawaxes': True, 'axescolor': (0, 0, 0),
       'point': 2, 'backg': (255, 255, 255)}

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

    if opt['drawaxes']:
        xcent, ycent, ticks = opt['width'] // 2, opt['height'] // 2, []
        for xtick in flrange(opt['xmin'], opt['xmax'] + 1, opt['xscl']):
            ticks.append(pixel(xtick, 0))
        for ytick in flrange(opt['ymin'], opt['ymax'] + 1, opt['yscl']):
            ticks.append(pixel(0, ytick))
        print ticks

        for l in xrange(ycent - opt['axes'] + 1, ycent + opt['axes']):
            for w in xrange(opt['width']):
                gpix[w, l] = opt['axescolor']
                if (w, l) in ticks:
                    for tw in xrange(w-1, w+2):
                        if 0 <= tw < opt['width']:
                            gpix[tw, l - opt['axes']] = opt['axescolor']
                            gpix[tw, l - opt['axes'] - 1] = opt['axescolor']
                            gpix[tw, l - opt['axes'] - 2] = opt['axescolor']
        for l in xrange(xcent - opt['axes'] + 1, xcent + opt['axes']):
            for h in xrange(opt['height']):
                gpix[l, h] = opt['axescolor']
                if (l, h) in ticks:
                    for th in xrange(h-1, h+2):
                        if 0 <= th < opt['height']:
                            gpix[l + opt['axes'], th] = opt['axescolor']
                            gpix[l + opt['axes'] + 1, th] = opt['axescolor']
                            gpix[l + opt['axes'] + 2, th] = opt['axescolor']

    graph.save(filename)

    while True:
        name = raw_input('\nFunction name: ')
        if name == '':
            break
        fn = raw_input('Function: ')
        colour = raw_input('Point color (r, g, b): ')
        exec name + ' = ' + fn
        exec 'colour = ' + colour

        # Decimal equivalent of one pixel
        pix = float(opt['xmax']-opt['xmin']) / float(opt['width'])

        # Iterate through all possible x values
        for val in flrange(opt['xmin'], opt['xmax'] + pix, pix):
            exec 'yval = ' + name + '.val(' + str(val) + ')'

            coords, point = pixel(val, yval), []
            # Thicken point by surrounding with a square
            if coords[1] is not None:
                pl, pr = coords[0] - opt['point'] + 1, coords[0] + opt['point']
                pt, pb = coords[1] - opt['point'] + 1, coords[1] + opt['point']
                point.append(coords)
                try:
                    for xc in xrange(pl, pr):
                        for yc in xrange(pt, pb):
                            point.append((xc, yc))
                except OverflowError:
                    pass

            for coord in point:
                validx = 0 <= coord[0] < opt['width']
                validy = 0 <= coord[1] < opt['height']
                if validx and validy and coords[1] is not None:
                    gpix[coord] = colour

        graph.save(filename)

    new = raw_input('\nNew graph [y/n]? ')
    if new == 'n':
        break
