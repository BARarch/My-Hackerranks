#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200327

def swapAdjacentBits(n):
    #print(list(map(lambda x: (n // (2 ** (2 * x)) % 4) , range(16))))
    return sum(map(lambda b: b[0] * b[1] ,zip(map(lambda a: 2 ** (2 * a), range(16)) , map(lambda y: (y * 2 + ((y * 2) // 4)) % 4 , map(lambda x: (n // (2 ** (2 * x))) % 4 , range(16))))))   

if __name__ == '__main__':
    import os
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())


    fptr.write(str(swapAdjacentBits(n)))
    fptr.write('\n')

    fptr.close()
