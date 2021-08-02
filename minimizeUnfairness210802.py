#Date Started: 210802 

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def maxMin(k, arr):
    from collections import deque
    kS = deque([])
    
    minUnfairness = max(arr)
    for num in sorted(arr):
        kS.append(num)
        if len(kS) > k:
            kS.popleft()
        if len(kS) == k:
            print(kS)
            unfairness = kS[-1] - kS[0]
            if unfairness < minUnfairness:
                minUnfairness = unfairness

    return minUnfairness

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
