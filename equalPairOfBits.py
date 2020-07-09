#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200328

def equalPairOfBits(n, m):
    return next(filter(lambda y: ((~(n ^ m)) // y) % 2, map(lambda x: 2 ** x, range(30))))
    
if __name__ == '__main__':
    import os
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    m = int(input())


    fptr.write(str(equalPairOfBits(n, m)))
    fptr.write('\n')

    fptr.close()
