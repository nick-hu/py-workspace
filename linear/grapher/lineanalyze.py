#!/usr/bin/python

from decimal import Decimal
import fractions as frac


class Linear():
    def __init__(self, mode, vals):
        fdata = [frac.Fraction(str(n)) for n in vals]
        data = []
        for n in vals:
            if '/' in n:
                flist = [x + '.0' for x in n.split('/')]
                data.append(flist[0] + '/' + flist[1])
            else:
                data.append(n)
        data = [Decimal(str(eval(n))) for n in data]

        if mode == 'p':
            self.eqn = [data[1], (data[1] * -1 * data[2]) + data[0]]
            self.feqn = [fdata[1], (fdata[1] * -1 * fdata[2]) + fdata[0]]
        elif mode == 'g':
            self.eqn = [(-1 * data[0]) / data[1], (-1 * data[2]) / data[1]]
            feqnnum = [(-1 * fdata[0]) / fdata[1]]
            self.feqn = feqnnum + [(-1 * fdata[2]) / fdata[1]]
        else:
            self.eqn = data
            self.feqn = fdata

    def pointform(self, xval=1):
        return [self.val(xval), self.slope(), float(xval)]

    def generalform(self):
        sfrac = [self.feqn[0].numerator, self.feqn[0].denominator]
        yfrac = [self.feqn[1].numerator, self.feqn[1].denominator]

        lcd = (sfrac[1] * yfrac[1]) / frac.gcd(sfrac[1], yfrac[1])
        aval = self.feqn[0] * lcd
        cval = self.feqn[1] * lcd

        return [float(aval), lcd * float(-1), float(cval)]

    def val(self, x):
        return float(self.eqn[0] * Decimal(str(x)) + self.eqn[1])

    def xint(self):
        if self.eqn[0] == Decimal('0') and self.eqn[1] == Decimal('0'):
            return 'Infinite solutions'
        elif self.eqn[0] == Decimal('0'):
            return 'No solution'
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
