#Date Started: 210727 

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def sunNum(a, b):
	return a + b

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    result = sunNum(a, b) 
    try:
        fptr.write(' '.join(map(str, iter(result))))
    
    except TypeError as te:
        fptr.write(str(result))
        
    fptr.write('\n')

    fptr.close()