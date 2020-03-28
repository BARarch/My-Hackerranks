#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200328

def fibs():
    a = 0
    yield a
    b = 1
    yield b

    while True:
        res = a + b
        a = b
        b = res
        yield res

def testFibs(n):
    f = fibs()
    #for i in range(n):
    odds = 0
    curr = next(f)
    while curr < n:
        if curr % 2:
            odds += curr
        curr = next(f)
    return odds

    
    


if __name__ == '__main__':
    import os
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(input())
    a = int(input())
    #b = int(input())


    fptr.write(str(testFibs(a)))
    fptr.write('\n')

    fptr.close()
