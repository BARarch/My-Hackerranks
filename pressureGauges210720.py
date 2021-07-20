#Date Started: 210720 

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def pressureGauges(morning, evening):
    return [list(map(min, zip(morning, evening))), list(map(max, zip(morning, evening)))]

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    result = pressureGauges(morning, evening) 
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()