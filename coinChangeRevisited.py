#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201008

import math
import os
import random
import re
import sys
import qtimer


# Complete the function below.
@qtimer.timeit
def coinChangeTop(n, coins):
    #print coins, n
    counts = [1] + [0] * n
    for c in coins:
        for i in range(len(counts)):
            if c + i <= n:
                counts[i + c] += counts[i]
    return counts[-1]


def getWaysGolf(n, c):
    ways = [0] * (n + 1)
    ways[0] = 1
    for coin in c:
        for index, _ in enumerate(ways):
            if coin <= index:
                ways[index] += ways[index - coin]
    return ways[n]


def getWays(n, c):
    coinsHash = {}
    return getWaysHelp(n, c, coinsHash)


def getWaysHelp(n, c, cH):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if n in cH:
        ct = tuple(c)
        if ct in cH[n]:
            return cH[n][ct]

    res = 0
    for i, coin in enumerate(c):
        res += getWaysHelp(n - coin, c[i:], cH)

    if n not in cH:
        cH[n] = {}
    cH[n][tuple(c)] = res

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = coinChangeTop(n, c)
    #print(ways)
    fptr.write(str(ways) + '\n')
    fptr.close()
