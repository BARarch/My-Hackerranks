

if __name__ == '__main__':
    import os
    import cs_utils
    fptr = open(os.environ['OUTPUT_PATH'], 'w')




    fptr.write("Hello Worlds")
    fptr.write('\n')

    fptr.close()