#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190829

#!/bin/python3

import os
import sys

#
# Complete the twoStacks function below.
#
def twoStacks_slow(x, a, b):
    #
    # Write your code here.
    #
    # binary search tree recusion, perfect test for backtracking
    # pick the lowest number first
    # i: position in stack a
    # j: position in stack b
    ## Select A
    from collections import deque

    moves = deque()
    maxD = 0
    moves.append((x, 0, 0, 0))

    def x_(move):
        return move[0]

    def d_(move):
        return move[1]

    def i_(move):
        return move[2]

    def j_(move):
        return move[3]

    pops = 0

    while moves:
        move = moves.popleft()
        pops += 1
        if d_(move) > maxD:
            maxD = d_(move)
        if i_(move) < len(a) and a[i_(move)] <= x_(move):
            # Add this move from this state: a draw from stack A
            moves.append((x_(move) - a[i_(move)], d_(move) + 1, i_(move) + 1, j_(move)))
        if j_(move) < len(b) and b[j_(move)] <= x_(move):
            # Add this move from this state: a draw from stack B
            moves.append((x_(move) - b[j_(move)], d_(move) + 1, i_(move), j_(move) + 1))

    print("x = " + str(x))
    print("Completed in " + str(pops) + "pops")
    return maxD

def twoStacks(x, a, b):
    ## This is two stacks
    ## with two actual stacks
    from collections import deque

    x1 = deque()
    # rolling sum for stack a only, this one is popped from the right side
    x2 = deque()
    # rolling sum for stack b only, this one is popped from the left side


    sum0 = 0
    x1.append(sum0)
    for num in a:
        if sum0 + num <= x:
            sum0 += num
            x1.append(sum0)
        else:
            break



    sum0 = 0
    #x2.append(sum0)
    for num in b:
        if sum0 + num <= x:
            sum0 += num
            x2.append(sum0)
        else:
            break

    dmax = len(x1) - 1
    d = dmax

    i = x1.pop()
    j = 0

    while x1 and x2:
        print("dmax pre is: " + str(dmax))
        j = x2.popleft()
        if i + j <= x:
            d += 1
            if d > dmax:
                dmax = d
        else:
            i = x1.pop()
            x2.appendleft(j)
            d -= 1
        print("dmax post is: " + str(dmax))

    if (not x1) and (i + j <= x):
        d += 1
        if d > dmax:
            dmax = d

    print("x1 has: " + str(len(x1)) + " x2 has: " + str(len(x2)))

    return dmax
        



        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
