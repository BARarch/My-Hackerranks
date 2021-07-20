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
def primesSum(a, b):
    return sum([x for x in functools.reduce(lambda primes, n: primes + [n,] if all(n % prime != 0 for prime in primes) else primes, range(3, b + 1, 2) , [2]) if x >= a])

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    result = primesSum(a, b) 
    fptr.write(str(result))
    fptr.write('\n')

    fptr.close()