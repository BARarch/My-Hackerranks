    #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    loses = []
    notImportant = []
    total = 0
    for weight, importance in contests:
        print("weight {}: importance {}".format(weight, importance))
        if importance:
            loses.append(weight)
        else:
            notImportant.append(weight)

    while len(loses) > k:
        deduct = min(loses)
        total -= deduct
        loses.remove(deduct)

    total += sum(loses)
    total += sum(notImportant)

    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
