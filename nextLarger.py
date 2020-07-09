#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190918

def nextLarger(a):
    from collections import deque

    largerQ = deque()
    solnQ = deque()

    def head(q):
        if len(q):
            return q[len(q) - 1]
        else:
            return -1

    for num in reversed(a):
        while head(largerQ) != -1 and head(largerQ) <= num:
            largerQ.pop()

        solnQ.appendleft(head(largerQ))
        largerQ.append(num)

    return list(solnQ)

        


if __name__ == '__main__':
    import os
    from cs_utils import *
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list_string_to_list(input())

    print("input: {}".format(a))


    fptr.write(list_to_string(nextLarger(a)))
    fptr.write('\n')

    fptr.close()
