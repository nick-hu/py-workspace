#!/usr/bin/python

from decimal import Decimal, ROUND_HALF_UP, getcontext
import math


class Function():
    def table(self, l):
        return dict(zip(l, map(self.val, l)))

    def trans(self, l):
        return map(self.val, l)


class Poly(Function):
    def __init__(self, coefs):
        coefs = [Decimal(str(c)) for c in coefs]
        deg = [Decimal(str(n)) for n in reversed(xrange(len(coefs)))]
        self.coefs = zip(coefs, deg)

    def val(self, x):
        y = Decimal(0)
        for c in self.coefs:
            if c[1] != 0:
                y = y + c[0] * Decimal(str(x)) ** c[1]
            else:
                y = y + c[0]
        return float(y)


class PolyTrans(Function):
    def __init__(self, deg, trans):
        self.deg = Decimal(str(deg))
        if trans == []:
            self.k, self.a = Decimal('0'), Decimal('1')
            self.b, self.h = Decimal('1'), Decimal('0')
        else:
            self.k, self.a = Decimal(str(trans[0])), Decimal(str(trans[1]))
            self.b, self.h = Decimal(str(trans[2])), Decimal(str(trans[3]))

    def val(self, x):
        x = Decimal(str(x))
        return float(self.a * (self.b * (x - self.h)) ** self.deg + self.k)


class Abs(Function):
    def __init__(self, f):
        self.f = f

    def val(self, x):
        return abs(self.f.val(x))


class Combined(Function):
    def __init__(self, f, g, op):
        self.f, self.g = f, g
        self.op = op

    def val(self, x):
        valf, valg = Decimal(str(self.f.val(x))), Decimal(str(self.g.val(x)))
        if self.op == '+':
            return float(valf + valg)
        elif self.op == '-':
            return float(valf - valg)
        elif self.op == '*':
            return float(valf * valg)
        elif self.op == '/':
            if self.g.val(x) == 0:
                return None
            return float(valf / valg)
        elif self.op == '@':
            if valg is None:
                return None
            return self.f.val(valg)


class Radical(Function):
    def __init__(self, f):
        self.f = f

    def val(self, x):
        if self.f.val(x) < 0:
            return None
        return math.sqrt(self.f.val(x))


class Exponent(Function):
    def __init__(self, trans):
        if len(trans) == 1:
            self.k, self.c, self.d = Decimal('0'), Decimal('1'), Decimal('1')
            self.x, self.h = Decimal(str(trans[0])), Decimal('0')
        else:
            self.k, self.c = Decimal(str(trans[0])), Decimal(str(trans[1]))
            self.a, self.d = Decimal(str(trans[2])), Decimal(str(trans[3]))
            self.h = Decimal(str(trans[4]))

    def val(self, x):
        x = Decimal(str(x))
        return float(self.c * self.a ** (self.d * x - self.h) + self.k)


class Log(Function):
    def __init__(self, trans):
        if len(trans) == 1:
            self.k, self.c, self.d = Decimal('0'), Decimal('1'), Decimal('1')
            self.a, self.h = Decimal(str(trans[0])), Decimal('0')
        else:
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
        if trans == []:
            self.a, self.b = Decimal('1'), Decimal('1')
            self.c, self.d = Decimal('0'), Decimal('0')
        else:
            self.a, self.b = Decimal(str(trans[0])), Decimal(str(trans[1]))
            self.c, self.d = Decimal(str(trans[2])), Decimal(str(trans[3]))

    def val(self, x):
        expr = self.b * Decimal(str(x)) - self.c
        exec 'trigval = math.' + self.f + "(Decimal('" + str(expr) + "'))"
        return float(self.a * Decimal(str(trigval)) + self.d)


class Point(Function):
    def __init__(self, d):
        self.d = d

    def val(self, x):
        if x in self.d:
            return float(self.d[x])
        else:
            return None


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


def deciround(n, p=2):
    n = Decimal(str(n))
    if p >= 1:
        p = Decimal('0.' + '0' * (p-1) + '1')
    else:
        p = Decimal('1' + '0' * (-1*(p+1)))
    return float(n.quantize(p, rounding=ROUND_HALF_UP))


def precision(p):
    getcontext().prec = p + 1
