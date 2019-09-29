#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190928

def nearestGreater(a):
    from collections import deque
    leftGreaterThan = deque()
    leftMost = []
    
    for i, n in enumerate(a):
        while leftGreaterThan:
            if n < leftGreaterThan[0][1]:
                leftMost.append(leftGreaterThan[0][0])
                #leftGreaterThan.appendleft((i, n))
                break
                
            else:
                leftGreaterThan.popleft()
      
        if not leftGreaterThan:
            leftMost.append(-1)
        leftGreaterThan.appendleft((i, n))
        
    return leftMost
