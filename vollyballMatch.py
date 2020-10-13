#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201012

import math
import os
import random
import re
import sys
import qtimer


# Complete the function below.
@qtimer.timeit
def vollyballOutcomes(a, b):
    if max(a, b) == 25:
        if a == 25:
            losingPoints = b
        elif b == 25:
            losingPoints = a
        if losingPoints < 24:
            return binom(25 + losingPoints - 1, losingPoints) % ((10**9) + 7)
        else:
            return 0
    elif max(a, b) > 25:
        if abs(a - b) != 2:
            return 0
        else:  # TieBreak
            if a > b:
                losingPoints = b
            else:
                losingPoints = a
            tieWays = binom(48, 24)
            return (tieWays * 2**(losingPoints - 24)) % ((10**9) + 7)
    else:
        return 0


def binom(n, k):
    return math.factorial(n) // math.factorial(k) // math.factorial(n - k)


if __name__ == "__main__":
    A = int(input())
    B = int(input())

    print(vollyballOutcomes(A, B))
