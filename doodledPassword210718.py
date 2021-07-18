#Date Started: 210718 

import math
import os
import random
import re
import sys
import qtimer

from collections import deque

# Complete the function below.
@qtimer.timeit
def doodledPassword(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    deque(map(lambda x: x[1].rotate(-x[0]), enumerate(res)), 0)
    return [list(d) for d in res]

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    
    result = doodledPassword(digits)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
