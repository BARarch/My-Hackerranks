#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200327

def differentRightmostBit(n, m):
    return list(filter(lambda y: ((n ^ m) // y) % 2, map(lambda x: 2 ** x, range(30))))[0]

if __name__ == '__main__':
    import os
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    m = int(input())

    fptr.write(str(differentRightmostBit(n, m)))
    fptr.write('\n')

    fptr.close()
