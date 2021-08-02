#Date Started: 210802 

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def commonChild(s1, s2):
    currentRow = [0, ] * (len(s2) + 1)
    for letterR in s1:
        lastRow = currentRow
        currentRow = [0, ] * (len(s2) + 1)
        for i, letterC in enumerate(s2):
            if letterC == letterR:
                currentRow[i + 1] = max(currentRow[i], lastRow[i + 1], lastRow[i] + 1)
            else:    
                currentRow[i + 1] = max(currentRow[i], lastRow[i + 1])

    return currentRow[-1]
            

    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
