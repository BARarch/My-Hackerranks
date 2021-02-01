#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201113

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def downToZero(n):
    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = downToZero(n)

        fptr.write(str(result) + '\n')

    fptr.close()
