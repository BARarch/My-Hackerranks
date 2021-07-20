#Date Started: 210720 

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def calcBonuses(bonuses, n):
    it = iter(bonuses)
    res = 0

    try:
        for _ in range(n):
            res += next(it)
    except StopIteration:
        res = 0

    return res


if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    result = calcBonuses(bonuses, n) 
    fptr.write(str(result))
    fptr.write('\n')

    fptr.close()