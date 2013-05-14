#!/usr/bin/python

from decimal import Decimal


class Function():
    def table(self, l):
        return dict(zip(l, map(self.val, l)))

    def trans(self, l):
        return map(self.val, l)


class Poly(Function):
    def __init__(self, *coefs):
        if type(coefs) == tuple and len(coefs) > 1:
            coefs = list(coefs)
        else:
            coefs = coefs[0]
        self.coefs = zip([float(c) for c in coefs], range(len(coefs))[::-1])

    def val(self, x):
        y = 0
        for c in self.coefs:
            y = y + c[0] * x ** c[1]
        return y


class Rational(Function):
    def __init__(self, f, g):
        self.f, self.g = f, g

    def val(self, x):
        if self.g.val(x) == 0:
            return None
        return self.f.val(x) / self.g.val(x)


def flrange(start, end, step=1.0):
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

# Examples
a = Poly(1, 0, 0)  # Quadratic
print a.val(32.2)  # 1036.84
print a.table([0, 1, 2])  # {0: 0.0, 1: 1.0, 2: 4.0}
print a.trans(range(3))  # [0.0, 1.0, 4.0]

b = Rational(Poly(1, 1, 3), Poly(1, 0))
print b.table(range(2))  # {0: None, 1: 5.0}

print [i for i in flrange(1, 2, 0.2)]
