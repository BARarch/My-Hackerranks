#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200419

def jumpStick(x, y):
    return 1


if __name__ == '__main__':
    import os
    from cs_utils import *
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    for _ in range(N):
        x, y = map(int, input().split(' '))
        fptr.write(str(jumpStick(x, y)))
        fptr.write('\n')


    #l = list_string_to_list(input())
    #ll = list_string_to_linked_list(input())
    #i = int(input())
    #s = input()

    #fptr.write(str())
    #fptr.write('\n')

    fptr.close()
