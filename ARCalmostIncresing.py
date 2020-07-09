#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190925

def almostIncreasingSequence(sequence): 
    if len(sequence) == 1:
        return True
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
        j += 1

    # j = 1, i = len(seq) - 1
    # i = len(seq) - j => j_prime
    j_prime = len(sequence) - j
    #print(len(sequence))
    #print(j)
    #print("i: {}, j_prime: {}".format(i, j_prime))
      
    if i == j_prime + 1:
        if i + 1 == len(sequence):
            ## Remove Last One
            print("...Remove Last One")
            return True
        if j_prime == 0:
            ## Remove first One
            print("...Remove First One")
            return True
        if sequence[j_prime] < sequence[i + 1] or sequence[j_prime - 1] < sequence[i]:
            ## Remove Either i Or j
            print("...Remove Either i Or j")
            return True
        return False
    else:
        return False

if __name__ == '__main__':
    import os
    from cs_utils import *
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    seq = list_string_to_list(input())

    print("input: {}".format(seq))


    fptr.write(str(almostIncreasingSequence(seq)))
    fptr.write('\n')

    fptr.close()
