#Date Started: 210730 

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def minimumBribes(q):
    from itertools import count
    c = count(1)
    pos0, pos1, pos2 = next(c), next(c), next(c)
    
    nBribes = 0
    for i in q:
        if i == pos0:
            pos0, pos1, pos2 = pos1, pos2, next(c)
        elif i == pos1:
            pos0, pos1, pos2 = pos0, pos2, next(c)
            nBribes += 1
        elif i == pos2:
            pos0, pos1, pos2 = pos0, pos1, next(c)
            nBribes += 2
        else:
            print("Too chaotic")
            return

    print(nBribes)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
