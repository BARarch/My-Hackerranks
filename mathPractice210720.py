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
def mathPractice(numbers):
    return functools.reduce(lambda a, b: a * b[0] + b[1], zip(numbers[::2], (numbers + [0,])[1::2]), 1)

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    result = mathPractice(numbers) 
    fptr.write(str(result))
    fptr.write('\n')

    fptr.close()