#Date Started: 210718 

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def startupName(companies):
    cmp1 = set(companies[0])
    cmp2 = set(companies[1])
    cmp3 = set(companies[2])
    res = cmp1.intersection(cmp2).union(cmp2.intersection(cmp3)).union(cmp3.intersection(cmp1)) - cmp1.intersection(cmp2).intersection(cmp3)
    return list(sorted(list(res)))

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    
    result = startupName(companies)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
