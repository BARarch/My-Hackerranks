#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190904

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedForest function below.
def balancedForest(c, edges):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        c = list(map(int, input().rstrip().split()))

        edges = []

        for _ in range(n - 1):
            edges.append(list(map(int, input().rstrip().split())))

        result = balancedForest(c, edges)

        fptr.write(str(result) + '\n')

    fptr.close()
