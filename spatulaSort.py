#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200419

def cookSort(R, S):

    return (R - 1) * (S - 1)

if __name__ == '__main__':
    import os
    from cs_utils import *
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())
    H = {}

    for n in range(N):
        R, S = map(int, input().split(' '))
        print("Case #{}: {}".format(n + 1, cookSort(R, S)))

    fptr.close()
