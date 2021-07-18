#Date Started: 210718 

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def transposeDictionary(scriptByExtension):
    return sorted([[scriptByExtension[i], i] for i in scriptByExtension], key=lambda x: x[0])

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    
    result = transposeDictionary(scriptByExtension)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
