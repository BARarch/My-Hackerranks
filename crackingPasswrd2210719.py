#Date Started: 210719 

import math
import os
import random
import re
import sys
import qtimer

from itertools import product

# Complete the function below.
@qtimer.timeit
def crackingPassword(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return sorted(list(filter(lambda x: int(x) % d == 0, map(createNumber, product(digits, repeat=k)))))

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    result = crackingPassword(digits, k, d) 
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()