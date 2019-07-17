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

    def in_order_itter_q(indexes, res, k):
        # Inorder Traversal with queue
        from collections import deque
        
        n = deque([1])
        level = deque([1])
        while n:
            #enter node
            if level[0] % k == 0:
                # perform swap on children
                swap(indexes, n[0])
            
            if left_child(node_at(indexes, n[0])) != -1:        ## if left child
                # save node to parent of left child queue
                n.appendleft(left_child(node_at(indexes, n[0])))
                level.appendleft(level[0] + 1)
                # enter left child node 
                continue
            while n:
                #backtrack into queue
                #append node to result: service the node inorder
                res.append(n[0])
                if right_child(node_at(indexes, n[0])) != -1:   ## if right child
                    # remove serviced node and level
                    nodeWithRightChild = n.popleft()
                    levelWithRightChild = level.popleft()
                    # enter right child node
                    n.appendleft(right_child(node_at(indexes, nodeWithRightChild))) 
                    level.appendleft(levelWithRightChild + 1)
                    break
                # remove serviced node
                n.popleft()
                level.popleft()
        



    outt = []
    for q in queries:
        #res = []
        #in_order_indexes(indexes, 1, res)
        #pre_order_swaps(indexes, 1, 1, q, res)
        #print(res)
        resQ = []
        in_order_itter_q(indexes, resQ, q)
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
