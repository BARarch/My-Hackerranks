import math
import os
import random
import re
import sys
from collections import deque

class TestCase:
    def __init__(self, fileName):
        f = open(fileName, 'r')
        RC = list(map(int, f.readline().rstrip().split(' ')))
        self.R = RC[0]
        self.C = RC[1]
        self.G = []
        for _ in range(self.R):
            self.G.append(f.readline().rstrip())

        rc = list(map(int, f.readline().rstrip().split(' ')))
        self.r = rc[0]
        self.c = rc[1]
        self.P = []
        for _ in range(self.r):
            self.P.append(f.readline().rstrip())

        f.close()

    def get_R(self):
        return self.R

    def get_C(self):
        return self.C

    def get_G(self):
        return self.G

    def get_r(self):
        return self.r

    def get_c(self):
        return self.c

    def get_P(self):
        return self.P

def make_row_Tracker(remaningRows):        
    def Tracker(col):
        ## Remember this is left to right
        for row in remaningRows:
            yield (row, col)
        yield 'YES'
    return Tracker

def row_check(row, seq):
    ## returns a list of indexies for the start of occuraces
    ## of seq in row
    res = []
    b = 0
    while True:
        start = row.find(seq)
        if start == -1:
            return res
        res.append(b + start)
        dist = start + 1
        b += dist
        row = row[dist:]

# Complete the gridSearch function below.
def gridSearch(G, P):
    # Make Row Tracker
    initSeq = P[0]
    rowTrack = make_row_Tracker(P[1:])
    currentTrackers = deque()
    R = len(G)
    r = len(P)
    c = len(P[0])

    n = 0
    for row in G:
        newTrackers = deque()
        while currentTrackers:
            tracker = currentTrackers.popleft()
            res = next(tracker)
            # Check for Termination
            if res == 'YES':
                return 'YES'

            seq = res[0]
            start = res[1]
            if row[start:start + c] == seq:
                ## Retain Tracker if it is still got
                newTrackers.append(tracker)

        if n < R - r + 1:
            newTrackers.extend(list(map(rowTrack, row_check(row, initSeq))))
        
        n += 1 
        currentTrackers = newTrackers

    ## Check Remaining Trackers
    while currentTrackers:
        tracker = currentTrackers.popleft()
        res = next(tracker)
        if res == 'YES':
            return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
