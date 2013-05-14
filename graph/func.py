#!/usr/bin/python


class Func():
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

    def table(self, l):
        return dict(zip(l, map(self.val, l)))

    def trans(self, l):
        return map(self.val, l)

a = Func(1, 0, 0)  # Quadratic
print a.val(32.2)  # 1036.84
print a.table([0, 1, 2])  # {0: 0.0, 1: 1.0, 2: 4.0}
print a.trans(range(3))  # [0.0, 1.0, 4.0]
