#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190608

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    dists = []
    prev = None
    for spaceStation in sorted(c):
        if prev != None:
            dists.append(spaceStation - prev)

        else:
            # The distance from the first space station and the first city
            pre = spaceStation
        
        prev = spaceStation

    #dont for get the last gap
    if len(dists) == 0:
        dists = [0]

    post = n - list(sorted(c))[-1] -  1

    return max([pre, max(dists) // 2, post])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
