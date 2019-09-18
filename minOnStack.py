#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190918

if __name__ == '__main__':
    import os
    from cs_utils import *
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list_string_to_list(input())

    print("input: {}".format(a))


    fptr.write(list_to_string(nextLarger(a)))
    fptr.write('\n')

    fptr.close()
