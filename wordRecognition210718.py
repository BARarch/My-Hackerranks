#Date Started: 210718 

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def wordsRecognition(word1, word2):
    def getIdentifier(w1, w2):
        return ''.join(sorted(set(w1) - set(w2)))

    return [getIdentifier(word1, word2), getIdentifier(word2, word1)]

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    
    result = wordsRecognition(word1, word2)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
