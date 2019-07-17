#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190711

import os
import sys

#
# Complete the swapNodes function below.
#


def swapNodes(indexes, queries):
    #print(indexes)
    #print(queries)
    #n_order_indexes(indexes, 1)
    def left_child(node):
        return node[0]

    def right_child(node):
        return node[1]

    def node_at(indexes, n):
        return indexes[n - 1]

    def swap(indexes, n):
        indexes[n - 1] = list(reversed(indexes[n - 1]))

    def in_order_indexes(indexes, n, res):
        if left_child(node_at(indexes, n)) != -1:
            in_order_indexes(indexes, left_child(node_at(indexes, n)), res)    
        res.append(n)
        if right_child(node_at(indexes, n)) != -1:
            in_order_indexes(indexes, right_child(node_at(indexes, n)), res)

    def pre_order_swaps(indexes, n, d, k, res):
        if (d % k == 0):
            # Perform Swap
            swap(indexes, n)
        if left_child(node_at(indexes, n)) != -1:
            pre_order_swaps(indexes, left_child(node_at(indexes, n)), d + 1, k, res)      
        res.append(n)
        if right_child(node_at(indexes, n)) != -1:
            pre_order_swaps(indexes, right_child(node_at(indexes, n)), d + 1, k, res)

    outt = []
    for q in queries:
        resIn = []
        pre_order_swaps(indexes, 1, 1, q, resIn)
        #res = []
        #in_order_indexes(indexes, 1, res)
        outt.append(resIn)
        
    return outt



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
