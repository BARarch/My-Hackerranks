#Date Started: 210718 

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def uniqueCharacters(document):
    return sorted(list(set(document)))

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    
    result = uniqueCharacters(document)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
