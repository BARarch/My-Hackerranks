#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200328

def countRomanXs(n):
    print(n)
    n = str(n)
    xs = 0
    if n[-1] == '9':
        xs += 1

    if len(n) > 1:
        d = n[-2]
        if int(d) % 5 == 4:
            xs += 1
        else:
            xs += int(d) % 5 
    return xs

def countInRange(a, b):
    return sum(map(countRomanXs, range(1, b + 1)))

if __name__ == '__main__':
    import os
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(input())
    a = int(input())
    b = int(input())


    fptr.write(str(countInRange(a, b)))
    fptr.write('\n')

    fptr.close()
