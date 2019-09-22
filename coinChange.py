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
    if n == 0:
        return 0  
    #if len(c) == 0:
    #    return 0
    #if n in c:
    #    a = c
    #    a.remove(n)
    #    return 1 + getWays(n, a)
    
    ways = 0
    for i in c:
        if n == i:
            ways += 1
        if n - i > 0:
            ways += getWays(n - i, c)

    #print(ways)
    return ways
    
def push_to_ways(n):
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)
    #print(ways)
    fptr.write(str(ways))
    fptr.close()

