#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201029

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def bfs(n, m, edges, s):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

