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
                break   
            else:
                leftGreaterThan.popleft()
      
        if not leftGreaterThan:
            leftMost.append(-1)
        leftGreaterThan.appendleft((i, n))

    rightGreaterThan = deque()
    rightMost = []

    for i, n in enumerate(reversed(a)):
        while rightGreaterThan:
            if n < rightGreaterThan[0][1]:
                rightMost.append(len(a) - rightGreaterThan[0][0] - 1)
                break
            else:
                rightGreaterThan.popleft()

        if not rightGreaterThan:
            rightMost.append(-1)
        rightGreaterThan.appendleft((i, n))
        
    rightMost = list(reversed(rightMost))

    res = []
    for i, n in enumerate(a):
        if leftMost[i] == -1:
            res.append(rightMost[i])
        elif rightMost[i] == -1:
            res.append(leftMost[i])
        else:
            leftDist = i - leftMost[i]
            rightDist = rightMost[i] - i
            if rightDist < leftDist:
                res.append(rightMost[i])
            else:
                res.append(leftMost[i])

    return res



if __name__ == '__main__':
    import os
    from cs_utils import *
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list_string_to_list(input())

    print("input: {}".format(a))


    fptr.write(str(nearestGreater(a)))
    fptr.write('\n')

    fptr.close()
