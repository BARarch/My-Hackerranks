#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200806

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def arrangeStudents(a, b):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = arrangeStudents(a, b)

        fptr.write(result + '\n')

    fptr.close()
