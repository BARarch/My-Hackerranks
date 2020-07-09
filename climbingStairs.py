#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190920

def climbingStairs(n):
    from collections import deque
    q = deque()
    q.append(n)
    summ = 0
    sums = {1: 1,
            2: 2}
    
    while q:
        s = q.pop()
        if s == 1:
            summ += 1
        elif s == 2:
            summ += 2
        else:
            if s in sums:
                if type(sums[s]) is int:
                    summ += sums[s]
                    #print('int hash sum added')
                else:
                    a = sums[sums[s][0]] + sums[sums[s][1]]
                    sums[s] = a
                    summ += a
                    #print('tuple sum added {}'.format(a))
            else:
                sums[s] = (s - 1, s - 2)
                q.append(s - 1)
                q.append(s - 2)

    #print(sums)
    return summ





if __name__ == '__main__':
    import os
    from cs_utils import *
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stairs = int(input())

    print("input: {}".format(stairs))


    fptr.write(str(climbingStairs(stairs)))
    fptr.write('\n')

    fptr.close()
