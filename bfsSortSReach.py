#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201029

import math
import os
import random
import re
import sys
import qtimer

from collections import deque
from collections import defaultdict


@qtimer.timeit
def bfs(n, m, edges, s):
    graph = defaultdict(list)
    for node1, node2 in edges:
        graph[node1].append(node2)
        graph[node2].append(node1)

    dists = defaultdict(lambda: -1)
    dists[s] = 0
    queue = [s]
    while queue:
        v = queue.pop(0)
        for neighbor in graph[v]:
            if dists[neighbor] < 0:
                queue.append(neighbor)
                dists[neighbor] = dists[v] + 6
    return [dists[i] for i in range(1, n + 1) if i != s]


# Complete the function below.
@qtimer.timeit
def bfsLoc(n, m, edges, s):
    M = {}

    for a, b in edges:
        #print(f'({a}, {b})')
        if a in M:
            M[a].append(b)
        else:
            M[a] = [
                b,
            ]

        if b in M:
            M[b].append(a)
        else:
            M[b] = [
                b,
            ]

    ## In undirected graph BFS does not back track
    V = set([s])

    def children(nodes):
        for node in nodes:
            if node not in V:
                yield node

    res = [-1] * (n + 1)
    res[0], res[s] = 0, 0

    if s in M:
        nodesToGo = deque([(6, children(M[s]))])
        while nodesToGo:
            dist, childNodes = nodesToGo.popleft()
            for node in childNodes:
                #if node not in V:
                res[node] = dist
                V.add(node)
                nodesToGo.append((dist + 6, children(M[node])))

    return [r for r in res if r != 0]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
