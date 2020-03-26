#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200326

def longestPath(fileSystem):
    print(fileSystem.split('\f'))
    return 1

if __name__ == '__main__':
    import os
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    fs = input()

    fptr.write(str(longestPath(fs)))
    fptr.write('\n')

    fptr.close()
