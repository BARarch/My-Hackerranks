#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201103

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
from fractions import Fraction
from functools import reduce

def product(fracs):
    t = # complete this line with a reduce statement
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
