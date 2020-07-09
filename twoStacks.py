#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190829

#!/bin/python3

import os
import sys

#
# Complete the twoStacks function below.
#

def twoStacks(x, a, b):
    sum0 = 0
    i = 1
    x1 = [0, ]
    while sum0 + a[i - 1] <= x:
        sum0 += a[i - 1]
        x1.append(sum0)
        i += 1
        if i - 1 == len(a):
            break
    
    sum0 = 0
    i = 1
    x2 = [0, ]
    while sum0 + b[i - 1] <= x:
        sum0 += b[i - 1]
        x2.append(sum0)
        i += 1
        if i - 1 == len(b):
            break


    i = len(x1) - 1
    dmax = i
    j = 0

    while i >= 0:
        while x1[i] + x2[j] <= x:
            if i + j > dmax:
                dmax = i + j
            j += 1
            if j == len(x2):
                break
        if j == len(x2):
            break
        i -= 1

    return dmax


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
