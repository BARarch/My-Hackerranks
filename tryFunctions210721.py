#Date Started: 210721 

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def tryFunctions(x, functions):
    return map(lambda f: eval(f)(x), functions)

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    result = tryFunctions(x, functions) 
    try:
        fptr.write('\n'.join(map(str, iter(result))))
    
    except TypeError as te:
        fptr.write(str(result))
        
    fptr.write('\n')

    fptr.close()