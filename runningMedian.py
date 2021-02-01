#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201016

import math
import os
import random
import re
import sys
import qtimer


# Complete the function below.
@qtimer.timeit
def runningMedian(a):
    from heapq import heappop, heappush, heapify

    low = []  # This is min Heap Multiply by -1
    heapify(low)

    def heappush_low(h, n):
        heappush(low, -1 * n)

    def heappop_low(h):
        return -heappop(h)

    high = []
    heapify(high)

    med = 0
    res = []
    for num in a:
        #place
        if num < med:
            heappush_low(low, num)
        else:
            heappush(high, num)

        #asses/shuffle
        if len(high) - len(low) == 2:
            heappush_low(low, heappop(high))
        elif len(low) - len(high) == 2:
            heappush(high, heappop_low(low))

        #compute med
        if len(high) > len(low):
            med = float(high[0])
        elif len(high) < len(low):
            med = float(-low[0])
        else:
            med = (high[0] - low[0]) / 2

        res.append(med)

    return map(lambda x: str(x), res)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
