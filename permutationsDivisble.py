#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201111

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
from itertools import permutations


@qtimer.timeit
def solve(n):
    if n == '0':
        return 'YES'  ## Stompper !
    for perm in permutations(n, 3 if len(n) > 3 else len(n)):
        if bin(int(''.join(perm)))[-3:] == '000':
            return 'YES'
    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = input()

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()
