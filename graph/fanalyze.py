#!/usr/bin/python

from math import log, ceil
from decimal import Decimal, ROUND_HALF_UP
from func import *


def root(f, a, b, p=2):
    assert cmp(f.val(a), 0) != cmp(f.val(b), 0)

    prec = Decimal(str(1.0 / 10**p))
    maxiter, i = ceil(log(Decimal(str(abs(b-a))) / prec, 2)), 1
    print maxiter
    while i <= maxiter:
        c = (Decimal(str(a)) + Decimal(str(b))) / Decimal('2.0')
        if f.val(c) == 0:
            return c.quantize(Decimal(prec), rounding=ROUND_HALF_UP)
        if cmp(f.val(a), 0) != cmp(f.val(c), 0):
            b = c
        else:
            a = c
        i = i + 1

    return c.quantize(Decimal(prec), rounding=ROUND_HALF_UP)


def intersect(f, g, a, b, p=2):
    h = Combined(f, g, '-')
    return root(h, a, b, p)
