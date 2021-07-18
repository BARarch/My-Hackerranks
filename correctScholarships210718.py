#Date Started: 210718 

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def correctScholarships(bestStudents, scholarships, allStudents):
    return  (set(bestStudents).intersection(set(scholarships)) == set(bestStudents)) and (set(scholarships).intersection(set(allStudents)) == set(scholarships)) and not (set(scholarships) == set(allStudents))

if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    
    result = correctScholarships(bestStudents, scholarships, allStudents)
    fptr.write(str(result))
    fptr.write('\n')

    fptr.close()
