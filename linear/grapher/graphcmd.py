#!/usr/bin/python

from math import pi, e
from decimal import Decimal
from itertools import product
import Image


def initialize(fname):
    global filename, graph, gpix, graphs

    filename = fname
    graph = Image.new('RGB', (opt['width'], opt['height']), opt['backg'])
    gpix = graph.load()  # Create image and pixel access object
    drawaxes()
    graphs = {}

    graph.save(filename)


def settings(newopt):
    global opt

    opt.update(newopt)


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


def flrange(start, end, step=Decimal('1.0')):
    if (start < end and step <= 0) or (start > end and step >= 0):
        return

    n, end, step = Decimal(str(start)), Decimal(str(end)), Decimal(str(step))
    if n < end:
        while n < end:
            yield float(n)
            n = n + step
    else:
        while n > end:
            yield float(n)
            n = n + step


def main(*prompt):
    global graph, graphs, gpix

    if prompt[0] == 'i':
        initialize(prompt[1])

    elif prompt[0] == 'f':
        graphs[prompt[1]] = (prompt[2], prompt[3])
        draw(prompt[1])

    elif prompt[0] == 's':
        settings(prompt[1])
        graph = Image.new('RGB', (opt['width'], opt['height']), opt['backg'])
        gpix = graph.load()
        drawaxes()
        for g in graphs:
            draw(g)

    elif prompt[0] == 'c':
        initialize(filename)

    graph.save(filename)

# Graph options (defaults)
opt = {'xmin': -20, 'xmax': 20, 'ymin': -20, 'ymax': 20,
       'width': 550, 'height': 550, 'xscl': 1, 'yscl': 1,
       'axes': 2, 'drawaxes': True, 'axescolor': (185, 225, 235),
       'tick': 2, 'grid': True, 'point': 2, 'backg': (255, 255, 255),
       'round': 0}
