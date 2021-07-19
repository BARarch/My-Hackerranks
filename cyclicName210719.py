#Date Started: 210719 

import math
import os
import random
import re
import sys
import qtimer

from itertools import cycle

# Complete the function below.
@qtimer.timeit
def cyclicName(name, n):
    gen = cycle(name)
    res = [str(next(gen)) for _ in range(n)]
    return ''.join(res)

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    
    result = cyclicName(name, n)
    fptr.write('\n' + result)
    fptr.write('\n')

    fptr.close()
