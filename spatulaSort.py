#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200419

if __name__ == '__main__':
    import os
    from cs_utils import *
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())
    H = {}

    for n in range(N):
        x, y = map(int, input().split(' '))
        print("Case #{}: {}".format(n + 1, jumpStick(x, y)))

    fptr.close()
