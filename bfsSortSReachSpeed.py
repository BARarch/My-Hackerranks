#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def bfs(n, m, edges, s):
    from collections import deque
    G = {x:[] for x in range(1, n + 1)}
    for edge in edges:
        G[edge[0]].append(edge[1])
        G[edge[1]].append(edge[0])
    
    C = deque([(c, 6) for c in G[s]])
    V = {s}

    res = [-1] * (n + 1)
    while C:
        node, dist = C.popleft()
        V.add(node)
        res[node] = dist
        for c in G[node]:
            if c not in V:
                C.append((c, dist + 6))
                
    return res[1:s] + res[s + 1:]
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
