#Date Started: 210720 

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def checkPassword(attempts, password):
    def check():
        while True:
            yield (yield) == password

    checker = check()
    for i, attempt in enumerate(attempts):
        next(checker)
        if checker.send(attempt):
            return i + 1

    return -1

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    result = checkPassword(attempts, password) 
    fptr.write(str(result))
    fptr.write('\n')

    fptr.close()