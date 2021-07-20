#Date Started: 210720 

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def correctLineup(athletes):
    return list(sum(zip(athletes[1::2], athletes[::2]), ()))

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    result = correctLineup(athletes) 
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()