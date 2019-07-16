#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190711

import os
import sys

#
# Complete the swapNodes function below.
#
def left_child(node):
    return node[0]

def right_child(node):
    return node[1]

def node_at(indexes, n):
    return indexes[n - 1]

def swapNodes(indexes, queries):
    #print(indexes)
    in_order_indexes(indexes, 1)
    return [[1]]

def in_order_indexes(indexes, n):
    if left_child(node_at(indexes, n)) != -1:
        in_order_indexes(indexes, left_child(node_at(indexes, n)))    
    print(n, end=" ")
    if right_child(node_at(indexes, n)) != -1:
        in_order_indexes(indexes, right_child(node_at(indexes, n)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
