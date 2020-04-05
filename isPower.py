#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200405

def isPower(n):
    from itertools import count
    print('Testing {}: '.format(n))
    if n == 1 or n == 0:
        return True

    for a in count(2): 
        if a == n:
            return False
        for b in count(2):
            if a ** b == n:
                return True
            if a ** b > n:
                break


if __name__ == '__main__':
    import os
    from cs_utils import *
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #l = list_string_to_list(input())
    #ll = list_string_to_linked_list(input())
    n = int(input())
    #s = input()

    fptr.write(str(isPower(n)))
    fptr.write('\n')

    fptr.close()
