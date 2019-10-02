#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternate function below.
def alternate(s):
    from itertools import combinations
    
    # Establish data structure as a hash of conbinations tuples, pointing to
    # tuples that represent the lengths of valid alternating strings
    # ('e', 'f') : ('f', 6) +> efefef 
    # the length of the string is 6 and the last charater in the sequence is 'f'
    # if the next encountered charater is an 'e', this key gets set to ('e', 7)
    # if the next encountered charater is an 'f', this key gets popped from the hash 
    # as it is no longer a valid alternating string

    combs = {x: None for x in combinations(set(s), 2)}
    print(s)

    # This shall do all the work
    for c in s:
        validSequences = tuple(filter(lambda x: c in x, combs.keys()))
        for sequence in validSequences:
            if combs[sequence] is None:
                combs[sequence] = (c, 1)
            elif combs[sequence][0] != c:
                combs[sequence] = [c, combs[sequence][1] + 1]
            else:
                combs.pop(sequence)
    print(combs)
    
    if len(combs) == 0:
        return 0
        
    # This shall loop through all remaining finding the longest sequence    
    return max(map(lambda x: x[1], combs.values()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
