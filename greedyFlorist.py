#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201027

import math
import os
import random
import re
import sys
import qtimer


# Complete the function below.
def sorted_costs(p):
    for c in sorted(p):
        yield c


@qtimer.timeit
def getMinimumCost(k, c):
    l = len(c) // k
    purchasesMax = len(c) % k
    cost = 0

    prices = sorted_costs(c)
    for _ in range(purchasesMax):
        cost += (l + 1) * next(prices)

    nPurchases = l
    while nPurchases > 0:
        for _ in range(k):
            cost += nPurchases * next(prices)
        nPurchases -= 1

    return cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
