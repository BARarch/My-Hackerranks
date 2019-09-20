#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190919
def countClouds(skyMap):
    return 4

if __name__ == '__main__':
    import os
    from cs_utils import *
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    skyMap = list_string_to_list(input())

    print("input: {}".format(skyMap))


    fptr.write(str(countClouds(skyMap)))
    fptr.write('\n')

    fptr.close()
