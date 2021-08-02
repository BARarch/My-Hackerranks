#Date Started: 210802 

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def freqQuery(queries):
    from collections import defaultdict
    numberToFreq = {}
    freqToNum = defaultdict(lambda: set())
    outs = []
    
    for com, elm in queries:
        if com == 1:
            # Insert into data struct
            if elm in numberToFreq:
                freqToNum[numberToFreq[elm]].remove(elm)
                numberToFreq[elm] += 1
                freqToNum[numberToFreq[elm]].add(elm)
            else:
                numberToFreq[elm] = 1
                freqToNum[1].add(elm)
        elif com == 2:
            # Delete from Data Struct
            if elm in numberToFreq:
                if numberToFreq[elm] > 1:
                    freqToNum[numberToFreq[elm]].remove(elm)
                    numberToFreq[elm] -= 1
                    freqToNum[numberToFreq[elm]].add(elm)
                else:
                    del numberToFreq[elm]
                    freqToNum[1].remove(elm)
                    
        elif com == 3:
            if len(freqToNum[elm]) > 0:
                outs.append(1)
            else:
                outs.append(0)

    return outs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
