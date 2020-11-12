#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201112

import math
import os
import random
import re
import sys
import qtimer


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


# Complete the function below.
def output_plates(plates):
    # Output Bs
    for row in plates:
        while row[1]:
            yield row[-1].pop()

    # Output As
    while plates[-1][0]:
        yield plates[-1][0].pop()


@qtimer.timeit
def waiter(number, q):
    primes = gen_primes()
    plates = [(number, [])]
    for i in range(q):
        A_minus_1 = plates[-1][0]
        A = []
        B = []
        prime = next(primes)
        while A_minus_1:
            if (A_minus_1[-1] % prime) == 0:
                B.append(A_minus_1.pop())
            else:
                A.append(A_minus_1.pop())
        plates.append((A, B))
    return output_plates(plates)
    #
    # Write your code here.
    #


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
