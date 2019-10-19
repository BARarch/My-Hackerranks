#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 191019

def nQueens(n):
    return [[5,5], [5,5]]

if __name__ == '__main__':
    import os
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    print("n: {}".format(n))

    fptr.write(str(nQueens(n)))
    fptr.write('\n')

    fptr.close()