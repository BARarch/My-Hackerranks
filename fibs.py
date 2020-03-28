#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200328

def palandrome3(n):
    def reverse(s): 
        str = "" 
        for i in s: 
            str = i + str
        return str

    return int(reverse(str(n)) + str(n))


def sumPalendromes():
    return sum(map(palandrome3, range(100)))
    


if __name__ == '__main__':
    import os
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(input())
    a = int(input())
    #b = int(input())


    fptr.write(str(sumPalendromes()))
    fptr.write('\n')

    fptr.close()
