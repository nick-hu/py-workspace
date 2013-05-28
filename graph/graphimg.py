#!/usr/bin/python

from math import pi, e
from itertools import product
import Image
from func import *
from fanalyze import *


def initialize():
    global filename, graph, gpix, graphs

    filename = raw_input('\nWrite graph to file: ')
    graph = Image.new('RGB', (opt['width'], opt['height']), opt['backg'])
    gpix = graph.load()  # Create image and pixel access object
    drawaxes()
    graphs = {}


def settings():
    print '\nCurrent graph options:\n', opt
    while True:
        setting = raw_input("\nChange option (option = value): ").split(' = ')
        if setting == ['']:
            break
        else:
            exec "opt['" + setting[0] + "'] = " + setting[1]
            print 'Graph options updated:\n', opt


def drawaxes():
    width, height = opt['width'], opt['height']
    xcent, ycent, ax = opt['width'] // 2, opt['height'] // 2, opt['axes']
    tkx = ycent if opt['grid'] else opt['tick'] + 2
    tky = xcent if opt['grid'] else opt['tick'] + 2

    if opt['drawaxes']:
        for pnt in product(xrange(width), xrange(ycent-ax+1, ycent+ax)):
            gpix[pnt[0], pnt[1]] = opt['axescolor']
        for pnt in product(xrange(xcent-ax+1, xcent+ax), xrange(height)):
            gpix[pnt[0], pnt[1]] = opt['axescolor']

        if opt['grid']:
            ax = ax - 1  # Thin out gridlines by 1
        for tk in flrange(opt['xmin'], opt['xmax']+1, opt['xscl']):
            pntx, pnty = pixel(tk, 0)
            tkw1, tkw2, tkh1, tkh2 = pntx-ax+1, pntx+ax, pnty-tkx+1, pnty+tkx
            for tkpnt in product(xrange(tkw1, tkw2), xrange(tkh1, tkh2)):
                if 0 <= tkpnt[0] < width and 0 <= tkpnt[1] < height:
                    gpix[tkpnt[0], tkpnt[1]] = opt['axescolor']

        for tk in flrange(opt['ymin'], opt['ymax']+1, opt['yscl']):
            pntx, pnty = pixel(0, tk)
            tkw1, tkw2, tkh1, tkh2 = pntx-tky+1, pntx+tky, pnty-ax+1, pnty+ax
            for tkpnt in product(xrange(tkw1, tkw2), xrange(tkh1, tkh2)):
                if 0 <= tkpnt[0] < width and 0 <= tkpnt[1] < height:
                    gpix[tkpnt[0], tkpnt[1]] = opt['axescolor']


def draw(name):
    # Decimal equivalent of one pixel
    pix = float(opt['xmax']-opt['xmin']) / float(opt['width'])

    # Iterate through all possible x values
    for val in flrange(opt['xmin'], opt['xmax'] + pix, pix):
        exec 'yval = graphs[' + repr(name) + '][0].val(' + str(val) + ')'
        if opt['round'] and yval is not None:
            yval = deciround(yval, opt['round'])

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
                gpix[coord] = graphs[name][1]


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
       'tick': 2, 'grid': False, 'point': 2, 'backg': (255, 255, 255),
       'round': 0}

initialize()
graph.save(filename)
while True:
    prompt = raw_input('\nNew image(i)/New function(f)/Analyze function(a)/' +
                       'Settings(s)/Quit(q): ')

    if prompt == 'i':
        initialize()

    elif prompt == 'f':
        while True:
            name = raw_input('\nFunction name: ')
            if name not in graphs:
                break
            print 'Error: Function name already in use'
        fn = raw_input('Function: ')
        col = raw_input('Point color (r,g,b): ')
        exec 'funcinst = ' + fn
        graphs[name] = (funcinst, tuple([int(x) for x in col.split(',')]))
        draw(name)

    elif prompt == 'a':
        for grph in graphs:
            exec "graphs['" + grph + "'] = " + str(graphs[grph])
        while True:
            afunc = raw_input('\nAnalysis: ')
            if afunc == '':
                break
            exec 'print ' + afunc

    elif prompt == 's':
        settings()
        graph = Image.new('RGB', (opt['width'], opt['height']), opt['backg'])
        gpix = graph.load()
        drawaxes()
        for g in graphs:
            draw(g)

    elif prompt == 'q':
        break

    graph.save(filename)
