#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200930

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def isBalanced(s):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
