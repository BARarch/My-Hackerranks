#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201106

import math
import os
import random
import re
import sys
import qtimer


# Complete the function below.
@qtimer.timeit
def gridSearch(G, P):

    for i, row in enumerate(G):
        if P[0] in row:
            starts = get_starts(row, P[0])

            for start in starts:
                j = 1
                while G[i + j][start:start + len(P[j])] == P[j]:
                    j += 1
                    if j == len(P):
                        return "YES"

    return 'NO'


def get_starts(S, p):
    start = 0
    res = []
    while start < len(S):
        if p == S[start:start + len(p)]:
            res.append(start)
        start += 1
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
