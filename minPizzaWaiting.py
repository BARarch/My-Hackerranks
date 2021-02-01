#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201009

import math
import os
import random
import re
import sys
import qtimer

# Complete the function below.
@qtimer.timeit
def minimumAverage(customers):
    from heapq import heappush, heappop

    customers.sort(reverse=True)

    N = len(customers)

    pq = []
    time_waiting = 0
    current_time = 0

    while customers or pq:
        while customers and customers[-1][0] <= current_time:
            heappush(pq, customers.pop()[::-1])
        if pq:
            current_task = heappop(pq)
            current_time += current_task[0]
            time_waiting += current_time - current_task[1]
        else:
            heappush(pq, customers.pop()[::-1])
            current_time = pq[0][1]

    return time_waiting // N

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    customers = []

    for _ in range(n):
        customers.append(tuple(map(int, input().rstrip().split())))

    result = minimumAverage(customers)

    fptr.write(str(result) + '\n')

    fptr.close()
