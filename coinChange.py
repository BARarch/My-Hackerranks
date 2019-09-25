#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190922

#!/bin/python3

## For every number < n there exists an optimal subproblem an sub solution for the coin-space
## get ways fills a hash with completed subproblems
#space[2,5,3,6]
#hsh = { 1: ||||
#        2: [2] |||
#        3: |[3] |||
#        4: [2 2] |||
#        5: |[2 3] |[5] ||
#        6: [2 2 2] |[3 3] |[6] |
#        7: |[2 2 3] |[2 5] ||
#        8: [2 2 2 2] |[2 3 3] |[5 3] |[2 6] |
#        9: |[3 3 3] [2 2 2 3] |[2 2 5] |[3 6] |
#       10: [2 2 2 2 2] |[2 2 3 3] |[5 5] [2 3 5] |[2 2 6] |}

import math
import os
import random
import re
import sys

# Complete the getWays function below.
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

    ways = getWays(n, c)
    #print(ways)
    fptr.write(str(ways)+'\n')
    fptr.close()

