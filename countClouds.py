#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190919

if __name__ == '__main__':
    import os
    from cs_utils import *
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    oppers = list_string_to_list(input())

    print("input: {}".format(oppers))


    fptr.write(list_to_string(minimumOnStack(oppers)))
    fptr.write('\n')

    fptr.close()
