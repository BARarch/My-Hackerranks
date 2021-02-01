#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200804

import math
import os
import random
import re
import sys
import qtimer


# Complete the function below.
@qtimer.timeit
def minimumMoves(s, d):
    from collections import deque
    s = deque(s)
    n = d
    d = 1 << d
    f = 0
    res = 0
    ## Initialize Comparison Fields
    for _ in range(n):
        f << 1
        f += int(s.popleft())

    while s:
        #print(f)
        if f == 0:
            f = 1
            res += 1

        f <<= 1
        f += int(s.popleft())
        f %= d

    ##Last One
    #print(f)
    if f == 0:
        res += 1

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    d = int(input().strip())

    result = minimumMoves(s, d)

    fptr.write(str(result) + '\n')

    fptr.close()
