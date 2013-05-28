#!/usr/bin/python

from math import log, ceil
from decimal import Decimal, ROUND_HALF_UP, getcontext
from func import *


def value(f, x, p=2):
    return deciround(f.val(x), p)


def root(f, a, b, p=2):
    assert cmp(f.val(a), 0) != cmp(f.val(b), 0)

    getcontext().prec = p + 1
    prec = Decimal(str(1.0 / 10**p))
    maxiter, i = ceil(log(Decimal(str(abs(b-a))) / prec, 2)), 1
    while i <= maxiter:
        c = (Decimal(str(a)) + Decimal(str(b))) / Decimal('2.0')
        if f.val(c) == 0:
            return deciround(c, p)
        if cmp(f.val(a), 0) != cmp(f.val(c), 0):
            b = c
        else:
            a = c
        i = i + 1

    return deciround(c, prec)


def intersect(f, g, a, b, p=2):
    h = Combined(f, g, '-')
    x = root(h, a, b, p)
    return deciround(x, p), deciround(f.val(x), p)


def fmin(f, a, b, p=2):
    a, b = Decimal(str(a)), Decimal(str(b))
    pr = Decimal('0.' + '0' * (p-1) + '1')
    n, nx = Decimal('0'), Decimal('0')
    for x in flrange(a, b, pr):
        if f.val(x) < n:
            n, nx = Decimal(str(f.val(x))), Decimal(str(x))
    return deciround(nx, p), deciround(n, p)


def fmax(f, a, b, p=2):
    a, b = Decimal(str(a)), Decimal(str(b))
    pr = Decimal('0.' + '0' * (p-1) + '1')
    n, nx = Decimal('0'), Decimal('0')
    for x in flrange(a, b, pr):
        if f.val(x) > n:
            n, nx = Decimal(str(f.val(x))), Decimal(str(x))
    return deciround(nx, p), deciround(n, p)
