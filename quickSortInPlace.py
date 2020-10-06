#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201005

import math
import os
import random
import re
import sys
import qtimer


# Complete the function below.
@qtimer.timeit
def quickSort(arr):
    def partition(arr, lo, hi):
        pivot = arr[hi - 1]
        print(pivot)
        i = lo
        for j in range(lo, hi - 1):
            if arr[j] < pivot:
                arr[i], arr[j] == arr[j], arr[i]
                i += 1
        arr[i], arr[hi - 1] = (arr[hi - 1], arr[i])
        print(arr)
        return i

    def quickSortHelp(arr, lo, hi):
        if lo < hi - 1:
            p = partition(arr, lo, hi)
            quickSortHelp(arr, lo, p)
            quickSortHelp(arr, p + 1, hi)q
        #print(arr)

    quickSortHelp(arr, 0, len(arr))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
