#Date Started: 210727 

import math
import os
import random
import re
import sys
import qtimer


class Functions(object):
    @classmethod
    def sign(cls, x):
        return -1 if x < 0 else 1

# Complete the function below.
@qtimer.timeit
def sign(x):
    return Functions.sign(x)

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    result = sign(x) 
    try:
        fptr.write(' '.join(map(str, iter(result))))
    
    except TypeError as te:
        fptr.write(str(result))
        
    fptr.write('\n')

    fptr.close()