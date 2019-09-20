#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190920

def climbingStairs(n):
    from collections import deque
    q = deque()
    q.append(n)
    summ = 0
    
    while q:
        if n == 1:
            summ += 1
        if n == 2:
            summ += 2
        else:
