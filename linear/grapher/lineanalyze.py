#!/usr/bin/python

from decimal import Decimal


class Linear():
    def __init__(self, mode, data):
        data = [Decimal(str(n)) for n in data]
        if mode == 'p':
            self.eqn = [data[1], (data[1] * -1 * data[2]) + data[0]]
        elif mode == 'g':
            self.eqn = [(-1 * data[0]) / data[1], (-1 * data[2]) / data[1]]
        else:
            self.eqn = data

    def pointform(self, xval=1):
        return [self.val(xval), self.slope(), float(xval)]

    def generalform(self):
        return [self.slope(), float(-1), self.yint()]

    def val(self, x):
        return float(self.eqn[0] * Decimal(str(x)) + self.eqn[1])

    def xint(self):
        if self.eqn[0] == Decimal('0') and self.eqn[1] == Decimal('0'):
            return 'Infinite solutions'
        elif self.eqn[0] == Decimal('0'):
            return None
        return float((Decimal('-1') * self.eqn[1]) / self.eqn[0])

    def yint(self):
        return float(self.eqn[1])

    def slope(self):
        return float(self.eqn[0])


class LinearSystem(Linear):
    def __init__(self, eqna, eqnb):
        newslope = eqna.eqn[0] - eqnb.eqn[0]
        newint = eqna.eqn[1] - eqnb.eqn[1]
        self.eqn = [newslope, newint]


def deciround(n, p=2):
    n = Decimal(str(n))
    if p >= 1:
        p = Decimal('0.' + '0' * (p-1) + '1')
    else:
        p = Decimal('1' + '0' * (-1*(p+1)))
    return float(n.quantize(p, rounding=ROUND_HALF_UP))
