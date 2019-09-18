#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190918

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    string = input()
    swaps = list_string_to_list(input())

    print("string: {}".format(string))
    print("swaps: {}".format(swaps))


    fptr.write(swapLexOrder(string, swaps))
    fptr.write('\n')

    fptr.close()
