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
def prefSum(a):
    return functools.reduce(lambda cum, elm: cum + [cum[-1] + elm,] if cum else [elm,], a, [])

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    result = prefSum(a) 
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()