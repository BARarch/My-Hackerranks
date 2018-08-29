from itertools import combinations_with_replacement

chars, k = input().split(' ')

for comb in combinations_with_replacement(sorted(chars), int(k)):
    print(''.join(comb))
