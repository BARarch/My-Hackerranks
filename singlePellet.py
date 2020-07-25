#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200725

import math
import os
import random
import re
import sys
import qtimer


# Complete the function below.
@qtimer.timeit
def singlePellet(n):
    def pellets(c):
        return c[0]

    def steps(c):
        return c[1]

    H = {n}
    from collections import deque
    q = deque([
        (n, 0),
    ])
    print("width: {}".format(len(str(n))))

    while q:
        c = q.popleft()
        if pellets(c) == 2:
            return steps(c) + 1

        if pellets(c) % 2 == 0:  ## even numbers divide by 2 add step
            n2 = pellets(c) // 2
            if n2 not in H:
                H.add(n2)
                q.append((n2, steps(c) + 1))

        else:
            nP = pellets(c) + 1
            if nP not in H:
                H.add(nP)
                q.append((nP, steps(c) + 1))
            nM = pellets(c) - 1
            if nM not in H:
                H.add(nM)
                q.append((nM, steps(c) + 1))

    return -1


if __name__ == "__main__":
    n = int(input())
    print(singlePellet(n))
