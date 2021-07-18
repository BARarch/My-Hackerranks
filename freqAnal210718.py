#Date Started: 210718 

import math
import os
import random
import re
import sys
import qtimer

from collections import Counter

# Complete the function below.
@qtimer.timeit
def frequencyAnalysis(encryptedText):
    return Counter(encryptedText).most_common()[0][0]

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    
    result = frequencyAnalysis(encryptedText)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
