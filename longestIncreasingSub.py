#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200807

import math
import os
import random
import re
import sys
import qtimer


# Complete the function below.
@qtimer.timeit
def longestIncreasingSubsequence(arr):
    def get_pos(num, arr):
        def get_pos_help(num, arr, start, stop):
            mid = (start + stop) // 2
            if num < arr[mid]:
                return get_pos_help(num, arr, start, mid)
            elif num > arr[mid]:
                return get_pos_help(num, arr, mid, stop)
            elif start == mid or stop == mid:
                return mid
            else:
                return mid

        return get_pos_help(num, arr, 0, len(arr))

    sortedArr = list(set(sorted(arr)))
    longestSeq = [-1] * len(sortedArr)
    maxx = 0

    for num in arr:
        pos = get_pos(num, sortedArr)
        curr = pos
        while curr >= 0 and (longestSeq[curr] == -1 or sortedArr[curr] == num):
            curr -= 1

        if curr == -1:
            longestSeq[pos] = 1
        else:
            longestSeq[pos] = longestSeq[curr] + 1

        if longestSeq[pos] > maxx:
            maxx = longestSeq[pos]

    return maxx


@qtimer.timeit
def longestIncreasingSubsequenceSlow(arr):
    class Node:
        def __init__(self, n, l):
            self.length = l
            self.tailValue = n
            self.prev = None
            self.next = None

        def set_prev(self, node):
            self.prev = node

        def set_next(self, node):
            self.next = node

    head = None
    for num in arr:
        if head is None:
            curr = Node(num, 1)
            head = curr
            end = curr

        else:
            curr = head
            newNode = None
            while not newNode:
                ## Step 1: Search Down Chain
                if curr is None:  # End of Chain
                    newNode = Node(num, 1)
                    end.set_next(newNode)  # <--Missed this
                    newNode.set_prev(end)
                    end = newNode
                elif num > curr.tailValue:
                    newNode = Node(num, curr.length + 1)
                    back = curr.prev
                    newNode.set_next(curr)
                    curr.set_prev(newNode)
                    ## Step 2: Search Back
                    while not newNode.prev:
                        if back is None:
                            head = newNode
                            ## Were done
                            break
                        elif newNode.length <= back.length:
                            newNode.set_prev(back)
                            back.set_next(newNode)
                        else:
                            back = back.prev
                    #print(newNode.length)
                else:
                    curr = curr.next

    #curr = head
    #while curr:
    #    print("{}: at lenth {}".format(curr.tailValue, curr.length))
    #    curr = curr.next
    return head.length


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = longestIncreasingSubsequence(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
