#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201103

import math
import os
import random
import re
import sys
import qtimer

from fractions import Fraction
from functools import reduce

# Complete the function below.
from operator import mul


@qtimer.timeit
def product(fracs):
    t = reduce(mul, fracs)
    return t.numerator, t.denominator


if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
