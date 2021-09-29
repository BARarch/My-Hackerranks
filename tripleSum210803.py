#Date Started: 210803 

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def triplets(a, b, c):
    b = list(sorted(set(b)))
    a = list(sorted(set(a)))
    c = list(sorted(set(c)))

    triplets = 0

    for center in b:
        left = 0
        right = len(a)
        midA = (left + right) // 2

        while left < midA:
            if a[midA] < center:
                left = midA
            elif a[midA] > center:
                right = midA
            else: 
                break
            midA = (left + right) // 2

        left = 0
        right = len(c)
        midC = (left + right) // 2

        while left < midC:
            if c[midC] < center:
                left = midC
            elif c[midC] > center:
                right = midC
            else:
                break
            midC = (left + right) // 2

        #print(f'for center {center}: indexes {midA} and {midC}')

        if a[midA] <= center:
            midA += 1
        if c[midC] <= center:
            midC += 1
        triplets += midA * midC

    return triplets

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
