#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200929

import math
import os
import random
import re
import sys
import qtimer


# Complete the function below.
@qtimer.timeit
def default():
    pass


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def conj(self):
        return Complex(self.real, -self.imaginary)

    def __mul__(self, no):
        a = self.real
        b = self.imaginary
        aN = no.real
        bN = no.imaginary
        return Complex((a * aN) - (b * bN), (a * bN) + b * aN)

    def __truediv__(self, no):
        quo = (no * no.conj()).real
        prod = self * no.conj()
        return Complex(prod.real / quo, prod.imaginary / quo)

    def mod(self):
        return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')
