#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201002

import math
import os
import random
import re
import sys
import qtimer


# Complete the function below.
@qtimer.timeit
def equalStacksOld(h1, h2, h3):
    def is_equal(H1, H2, H3):
        return H1 == H2 == H3

    H = [sum(h1), sum(h2), sum(h3)]
    stacks = [list(reversed(h)) for h in [h1, h2, h3]]

    while not is_equal(*H):
        H = [
            h - s.pop() if isMax else h
            for h, s, isMax in zip(H, stacks, (max(H) == h for h in H))
        ]

    return H[0]


@qtimer.timeit
def equalStacks(h1, h2, h3):
    # Write your code here
    a = [h1, h2, h3]
    while len((set([sum(a[0]), sum(a[1]), sum(a[2])]))) > 1:
        maxsum = max(sum(a[0]), sum(a[1]), sum(a[2]))
        index = [i for i in range(3) if maxsum == sum(a[i])]
        a[index[0]] = a[index[0]][1:]
    return sum(a[0])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
