#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190727


def solution(l):
    inds = {}

    ## n^2 factor indexing
    for ind in range(len(l)):
        inds[ind] = []
        for j in range(ind + 1, len(l)):
            if l[j] % l[ind] == 0:
                inds[ind].append(j)

    def print_inds(inds):
        for ind in inds:
            print(str(ind) + ": " + ' '.join(map(str, inds[ind])))

    
    
    print(l)
    print_inds(inds)

    ## Count up lucky triplet paths
    tot = 0
    for ind in inds:        
        for j in inds[ind]:
            tot += len(inds[j])

    def print_lucky_triplets():
        pass

    return tot

if __name__ == '__main__':
    import os
    import sys

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    codes = list(map(int, input().split(' ')))
    result = solution(codes)

    fptr.write(str(result) + '\n')

    fptr.close()
