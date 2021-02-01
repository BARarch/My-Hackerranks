#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201021

import math
import os
import random
import re
import sys
import qtimer


# Complete the function below.
@qtimer.timeit
def solve(n):
    if math.sqrt(1 + (8 * n)).is_integer():
        return f'Go On Bob {int((math.sqrt(1 + (8 * n)) - 1) // 2)}'
    return "Better Luck Next time"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()
