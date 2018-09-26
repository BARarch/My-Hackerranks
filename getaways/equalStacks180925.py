#!/bin/python3

import os
import sys
from collections import deque

#
# Complete the equalStacks function below.
#

def equalStacks(h1, h2, h3):
    stacks = [deque(h1), deque(h2), deque(h3)]
    sums = list(map(sum, stacks))
    shortest = min(sums)
    matches = 1
    
    i = 0
    while True:
        i %= 3
        if shortest <= 0:
            return 0
        
        while sums[i] > shortest:
            sums[i] -= stacks[i].popleft()
            
        if sums[i] < shortest:  ## Reset Shortests and Counts
            shortest = sums[i]
            matches = 1
        else:                   ## The sum is the same as shortest
            matches += 1
            if matches == 3:    ## Terminal Case
                return shortest
        
        i += 1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
