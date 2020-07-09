#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200417
def crosswordFormation(words):
    def count_out(AB, AD, CB, CD):
        count = 0
        for ab in AB:
            for ad in AD:
                for cb in CB:
                    for cd in CD:
                        if (((ab[0] - ad[0]) == (cb[0] - cd[0])) and
                             (abs(ab[0] - ad[0]) > 1) and
                            ((ab[1] - cb[1]) == (ad[1] - cd[1])) and
                             (abs(ab[1] - cb[1]) > 1)):
                           count += 1
        return count
    
    #print(words)
    def n_combs(a, b):
        combs = []
        for i, ch1 in enumerate(a):
            for j, ch2 in enumerate(b):
                if ch1 == ch2:
                    combs.append((i, j))
        return combs

    A, B, C, D = words[0], words[1], words[2], words[3]

    def swap_run(A, B, C, D):
        H = {   A: {B: [], D: []},
                C: {B: [], D: []}}
        
        for a in H:
            for b in H[a]:
                H[a][b] = n_combs(a, b)

        return count_out(H[A][B], H[A][D], H[C][B], H[C][D])

    res = 0
    res += swap_run(words[0], words[1], words[2], words[3]) * 2 #2 For rotation
    res += swap_run(words[0], words[2], words[3], words[1]) * 2 #2 For rotation
    res += swap_run(words[0], words[3], words[1], words[2]) * 2 #2 For rotation

    return res


if __name__ == '__main__':
    import os
    from cs_utils import *
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = list_string_to_list(input())
    #ll = list_string_to_linked_list(input())
    #i = int(input())
    #s = input()

    fptr.write(str(crosswordFormation(l)))
    fptr.write('\n')

    fptr.close()

