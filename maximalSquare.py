#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 191019

def maximalSquare(matrix):
    print(len(matrix))
    return 1

import cs_utils
import os

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    mat = cs_utils.list_string_to_list(input())

    fptr.write(str(maximalSquare(mat)))
    fptr.write('\n')

    fptr.close()