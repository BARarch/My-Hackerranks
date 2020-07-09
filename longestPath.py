#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200326

def longestPath(fileSystem):
    lengths = [0]
    maxPathLength = 0
    for doc in fileSystem.split("\\f"):
        print("doc: " + str(doc))
        rowPath = doc.split("\\t")
        level = len(rowPath)
        elemName = rowPath[-1]

        if "." in elemName: # It is a file
            # Compute Path Length
            lengths = lengths[:level]                   # leave the last one at the end it is the current 
            length = lengths[-1] + len(elemName)
            print(lengths)
            print(elemName)
            print("Level " + str(level))
            print(length)
            if length > maxPathLength:
                maxPathLength = length
                
        else:               # It is a directory
            lengths = lengths[:level]
            lengths.append(lengths[-1] + len(elemName) + 1) # +1 for slash

    return maxPathLength

if __name__ == '__main__':
    import os
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    fs = input()

    fptr.write(str(longestPath(fs)))
    fptr.write('\n')

    fptr.close()
