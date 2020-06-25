#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200625

import math
import os
import random
import re
import sys

# Complete the lilysHomework function below.
def lilysHomework(arr):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

