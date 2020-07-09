#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200625

import math
import os
import random
import re
import sys
from qtimer import timeit


# Complete the lilysHomework function below.
@timeit
def lilysHomework(arr):
    from collections import deque

    def swapSort_one_way(arr1):
        A = sorted(arr1)

        H = {val: index for index, val in enumerate(arr1)}
        swaps = 0
        for i in range(len(arr1)):
            if arr1[i] != A[i]:
                swaps += 1
                j = H[A[i]]
                H[arr1[i]] = H[A[i]]
                arr1[i], arr1[j] = A[i], arr1[i]

        return swaps

    ## create hashmap value -> index
    def swapSort(arr1):
        A = deque(sorted(arr1))
        H = {val: index for index, val in enumerate(arr1)}

        #H1 = {}
        #for index, val in enumerate(arr1):
        #    if val in H1:
        #        H1[val].append(index)
        #        print("Arr has a reapeat: {}".format(val))
        #    else:
        #
        #        H1[val] = [
        #            index,
        #        ]
        #print(len(H))
        #print(len(H1))

        start = 0
        end = len(arr) - 1
        swaps = 0
        #print(arr1)
        while start < end:
            maxNum = A.pop()
            minNum = A.popleft()
            if end != H[maxNum]:
                #Perform Max Swap
                a = arr1[end]
                arr1[end] = maxNum
                arr1[H[maxNum]] = a
                H[a] = H[maxNum]
                H[maxNum] = end
                swaps += 1
            if start != H[minNum]:
                #Perform Min Swap
                a = arr[start]
                arr1[start] = minNum
                arr1[H[minNum]] = a
                H[a] = H[minNum]
                H[minNum] = start
                swaps += 1

            start += 1
            end -= 1
            #print(arr1)
        return swaps

    a = swapSort_one_way(list(arr))
    print(a)
    b = swapSort_one_way(list(reversed(arr)))
    print(b)
    return min(a, b)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
