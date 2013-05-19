#!/usr/bin/python

from decimal import Decimal
import math


class Function():
    def table(self, l):
        return dict(zip(l, map(self.val, l)))

    def trans(self, l):
        return map(self.val, l)


class Poly(Function):
    def __init__(self, coefs):
        coefs = [Decimal(str(c)) for c in coefs]
        deg = [Decimal(str(n)) for n in range(len(coefs))[::-1]]
        self.coefs = zip(coefs, deg)

    def val(self, x):
        y = Decimal(0)
        for c in self.coefs:
            if c[1] != 0:
                y = y + c[0] * Decimal(str(x)) ** c[1]
            else:
                y = y + c[0]
        return float(y)


class Rational(Function):
    def __init__(self, f, g):
        self.f, self.g = f, g

    def val(self, x):
        if self.g.val(x) == 0:
            return None
        return self.f.val(x) / self.g.val(x)


class Radical(Function):
    def __init__(self, f):
        self.f = f

    def val(self, x):
        if self.f.val(x) < 0:
            return None
        return math.sqrt(self.f.val(x))


class Exponent(Function):
    def __init__(self, trans):
        self.k, self.c = Decimal(str(trans[0])), Decimal(str(trans[1]))
        self.a, self.d = Decimal(str(trans[2])), Decimal(str(trans[3]))
        self.h = Decimal(str(trans[4]))

    def val(self, x):
        x = Decimal(str(x))
        return float(self.c * self.a ** (self.d * x - self.h) + self.k)


class Log(Function):
    def __init__(self, trans):
        self.k, self.c = Decimal(str(trans[0])), Decimal(str(trans[1]))
        self.a, self.d = Decimal(str(trans[2])), Decimal(str(trans[3]))
        self.h = Decimal(str(trans[4]))

    def val(self, x):
        x = Decimal(str(x))
        if self.d * (x - self.h) <= 0:
            return None
        if self.a == Decimal('10'):
            logval = Decimal(str(math.log10(self.d * (x - self.h))))
            return float(self.c * logval + self.k)
        logval = Decimal(str(math.log(self.d * (x - self.h), self.a)))
        return float(self.c * logval + self.k)


class Trig(Function):
    def __init__(self, f, trans):
        self.f = f
        self.a, self.b = Decimal(str(trans[0])), Decimal(str(trans[1]))
        self.c, self.d = Decimal(str(trans[2])), Decimal(str(trans[3]))

    def val(self, x):
        expr = self.b * Decimal(str(x)) - self.c
        exec 'trigval = math.' + self.f + "(Decimal('" + str(expr) + "'))"
        return self.a * Decimal(str(trigval)) + self.d


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


def prec(n):
    decimal.getcontext().prec = n

# Examples
'''
a = Poly([1, 0, 0])  # Quadratic
print a.val(32.2)  # 1036.84
print a.table([0, 1, 2])  # {0: 0.0, 1: 1.0, 2: 4.0}
print a.trans(range(3))  # [0.0, 1.0, 4.0]

b = Rational(Poly([1, 1, 3]), Poly([1, 0]))
print b.table(range(2))  # {0: None, 1: 5.0}
'''
