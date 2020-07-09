#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190918

def minimumOnStack(operations):
    soln = []
    from collections import deque
    a = deque()

    for opper in operations:
        call = opper.split(' ')
        if call[0] == "push":
            a.append(int(call[1]))
        elif call[0] == "pop":
            a.pop()
        elif call[0] == "min":
            soln.append(min(a))

    return soln

if __name__ == '__main__':
    import os
    from cs_utils import *
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    oppers = list_string_to_list(input())

    print("input: {}".format(oppers))


    fptr.write(list_to_string(minimumOnStack(oppers)))
    fptr.write('\n')

    fptr.close()
