#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190922

if __name__ == '__main__':
    import os
    from cs_utils import *
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nums = list_string_to_list(input())

    print("input: {}".format(nums))


    fptr.write(str(houseRobber(nums)))
    fptr.write('\n')

    fptr.close()
