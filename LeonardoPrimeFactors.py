## LeonardoPrimeFactors

import math
from operator import itemgetter
import os
import random
import re
import sys
import qtimer
import itertools
import operator



def gen_primes():
    D = {}
    q = 2

    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

# Watch Boundary Conditions
def primeCountOld(n):
    lessThanRange = itertools.accumulate(gen_primes(), operator.mul)
    r = next(lessThanRange)
    res = 0

    while r <= n:
        r = next(lessThanRange)
        res += 1

    return res

def primeCount(n):
    lessThanRange = zip(itertools.count(),itertools.accumulate(gen_primes(), operator.mul))
    res, r = next(lessThanRange)

    while r <= n:
        res, r = next(lessThanRange)

    return res
    

    


if __name__ == "__main__":

    sys.stdin = open(sys.argv[1])

    q = int(input().strip())
    
    for q_itr in range(q):
        n = int(input().strip())

        result = primeCount(n)

        print(n, end=" ")
        print(result)
        

        #fptr.write(str(result) + '\n')
