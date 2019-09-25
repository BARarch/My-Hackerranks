#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190925

def almostIncreasingSequence(sequence):

    
    # Seq 1
    prev = sequence[0]
    i = 1
    while i < len(sequence) and sequence[i] > prev:
        prev = sequence[i]
        i += 1

    prevRev = sequence[-1]
    j = 2
    while j < 1 + len(sequence) and sequence[-j] < prevRev:
        prevRev = sequence[-j]
        j += i

    # j = 1, i = len(seq) - 1
    # i = len(seq) - j => j_prime
    j_prime = len(sequence) - j

    print("i: {} j_prime: {}".format(i, j_prime))

     

        
    return i == j_prime + 1

if __name__ == '__main__':
    import os
    from cs_utils import *
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    seq = list_string_to_list(input())

    print("input: {}".format(seq))


    fptr.write(str(almostIncreasingSequence(seq)))
    fptr.write('\n')

    fptr.close()
