#Date Started: 210719 

import math
import os
import random
import re
import sys
import qtimer

from itertools import chain, repeat, dropwhile

# Complete the function below.
@qtimer.timeit
def memoryPills(pills):
    gen = chain(dropwhile(lambda x: len(x) % 2 == 1, pills), repeat(""))
    next(gen)
    return [next(gen) for _ in range(3)]

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    
    result = memoryPills(pills)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
