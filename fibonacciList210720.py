#Date Started: 210720 

import math
import os
import random
import re
import sys
import qtimer

import functools

# Complete the function below.
@qtimer.timeit
def fibonacciList(n):
    return [[0] * x for x in functools.reduce(lambda a, b: a + (a[-2] + a[-1],), range(n - 2), (0, 1))]

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    result = fibonacciList(n) 
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()