#Date Started: 210727 

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def sortCodesignalUsers(users):
    res = [CodeSignalUser(*user) for user in users]
    res.sort(reverse=True)
    return list(map(str, res))

class CodeSignalUser(object):
    def __init__(self, name, ids, score):
        self.name = name
        self.id = int(ids)
        self.xps = int(score)

    def __lt__(self, other):
        return self.xps < other.xps if self.xps != other.xps else self.id > other.id 
        
    def __str__(self):
        return self.name

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    result = sortCodesignalUsers(users) 
    if isinstance(result, int) or isinstance(result, str):
        fptr.write(str(result))
    elif isinstance(result, list) or isinstance(result, tuple):
        fptr.write(str(result))
    else:
        fptr.write(' '.join(map(str, iter(result))))
        
    fptr.write('\n')

    fptr.close()