#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200327

if __name__ == '__main__':
    import os
    fptr = open(os.environ['OUTPUT_PATH'], 'w')




    fptr.write("Hello Worlds")
    fptr.write('\n')

    fptr.close()
