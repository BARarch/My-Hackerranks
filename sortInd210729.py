#Date Started: 210729 

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def sortInd(inp):
    ## Create Two Stacks:
    ## One for the subsequence storted at the beginning of the array and another for the subsequence at the end
    preSorted = [inp[0],]
    i = 1
    while inp[i] >= preSorted[-1]:
        preSorted.append(inp[i])
        i += 1

    i = 2
    postSorted = [inp[-1],]
    while inp[-i] <= postSorted[-1]:
        postSorted.append(inp[-i])
        i += 1

    ## Start a list of unsorted elements in the array as the elements that are not in either preSorted or postSorted
    unsorted = inp[len(preSorted):-len(postSorted)]

    
    ## Now Begin Step in reverse
    ## Remove from the pre and post sorted stacks until the min of the unsorted stack is greater than or equal to the end of the preSorted sequence
    ## and the max of the unsorted stack as less than or equal to the beginning of the postSorted sequence.
    while (preSorted and min(unsorted) < preSorted[-1]) or (postSorted and max(unsorted) > postSorted[-1]):
        if preSorted and min(unsorted) < preSorted[-1]:
            unsorted.append(preSorted.pop())
        if postSorted and max(unsorted) > postSorted[-1]:
            unsorted.append(postSorted.pop())

    return len(preSorted), len(inp) - len(postSorted) - 1


if __name__ == "__main__":
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for var, exp in cs_utils.dict_statement_reader(sys.stdin):
        exec(var + " = " + exp)

    result = sortInd(inp) 
    if isinstance(result, int) or isinstance(result, str):
        fptr.write(str(result))
    elif isinstance(result, list) or isinstance(result, tuple):
        fptr.write(str(result))
    else:
        fptr.write(' '.join(map(str, iter(result))))
        
    fptr.write('\n')

    fptr.close()