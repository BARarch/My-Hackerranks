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
            # Perform Preorder Swap
            swap(indexes, n)
        if left_child(node_at(indexes, n)) != -1:
            pre_order_swaps(indexes, left_child(node_at(indexes, n)), d + 1, k, res)      
        # Perform Inorder Print
        res.append(n)
        if right_child(node_at(indexes, n)) != -1:
            pre_order_swaps(indexes, right_child(node_at(indexes, n)), d + 1, k, res)

    def in_order_itter_q(indexes, res):
        # Inorder Traversal with queue
        from collections import deque
        
        n = deque([1])
        #level = deque([1])
        while n:
            #enter node
            #if left child
            if left_child(node_at(indexes, n[0])) != -1:
                # save node to parent of left child queue
                n.appendleft(left_child(node_at(indexes, n[0])))
                # enter left child node 
                continue
            while n:
                #append node to result: service the node inorder
                res.append(n[0])
                if right_child(node_at(indexes, n[0])) != -1:
                    # enter right child node
                    nodeWithRightChild = n.popleft()
                    n.appendleft(right_child(node_at(indexes, nodeWithRightChild))) 
                    break
                # pop from parent of left child queue
                n.popleft()
        



    outt = []
    for q in queries:
        res = []
        #pre_order_swaps(indexes, 1, 1, q, res)
        in_order_indexes(indexes, 1, res)
        print(res)
        resQ = []
        in_order_itter_q(indexes, resQ)
        #in_order_indexes_iter(indexes, resIter)
        #pre_order_swaps_iter(indexes, q, resIter)
        #res = []
        #in_order_indexes(indexes, 1, res)
        outt.append(resQ)
        
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
