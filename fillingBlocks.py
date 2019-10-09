#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 191008

def fillingBlocks(n):
    blocksHash = {0: 1}

    def fillingBlocksHelp(n):
        if n in blocksHash:
            return blocksHash[n]

        fits = 0

        for i in range(n):
            j = n - i
            if j == 1:
                fits += fillingBlocksHelp(i)
            elif j == 2:
                fits += 4 * fillingBlocksHelp(i)
            elif j % 2: # j is odd, there are 2 indivisibles
                fits += 2 * fillingBlocksHelp(i)
            else:  # j is even, there are 3 indivisibles
                fits += 3 * fillingBlocksHelp(i)

        blocksHash[n] = fits    
        return fits

    return fillingBlocksHelp(n)

    
    

    

if __name__ == '__main__':
    import os
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    print("n: {}".format(n))

    fptr.write(str(fillingBlocks(n)))
    fptr.write('\n')

    fptr.close()
