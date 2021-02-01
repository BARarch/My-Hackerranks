#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 201104

import math
import os
import random
import re
import sys
import qtimer


# Complete the function below.
@qtimer.timeit
def passtraffic():
    pass


from collections import defaultdict
if __name__ == "__main__":
    N = int(input())
    H = defaultdict(list)
    for _ in range(N):
        line = input().split(' ')
        month, traffic = int(line[0].split('_')[-1]), int(line[-1])
        H[month].append(traffic)

    for m in range(1, 13):
        print(sum(H[m]) / len(H[m]))
