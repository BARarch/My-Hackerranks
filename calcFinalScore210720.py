#Date Started: 210720 

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def calcFinalScore(scores, n):
    gen = (score ** 2 for score in reversed(sorted(scores)))

    res = 0
    try:
        for _ in range(n):
            res += next(gen)
    except StopIteration:
        res //= 5

    return res


if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    result = calcFinalScore(scores, n) 
    fptr.write(str(result))
    fptr.write('\n')

    fptr.close()