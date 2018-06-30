#!/bin/python3

import os
import sys

#
# Complete the dynamicArray function below.
#


def dynamicArray(n, queries):
    #
    # Write your code here.
    #
    
    S = {i: [] for i in range(n)}
    
    lastAnswer = 0
    res = []
    for query in queries:
        #print(query)
        q = query[0]
        x = query[1]
        y = query[2]
        
        
        if q == 1:
            S[(x ^ lastAnswer) % n].append(y) 
            #print('type1')
            #print(S)
        else:
            #print('type2')
            seq = S[(x ^ lastAnswer) % n]
            lastAnswer = seq[y % len(seq)]
            #print(lastAnswer)
            res.append(lastAnswer)
            #print(res)
            
    return res
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)
    #print(result)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
