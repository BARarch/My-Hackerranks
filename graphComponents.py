#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190904

#!/bin/python3

import os
import sys

#
# Complete the componentsInGraph function below.
#
def componentsInGraph(gb):
    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = componentsInGraph(gb)

    fptr.write(' '.join(map(str, SPACE)))
    fptr.write('\n')

    fptr.close()

