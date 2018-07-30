from itertools import combinations

f = input().split(' ')
string = sorted(f[0])
K = int(f[1])

for k1 in range(K):
    k = k1 + 1
    for comb in combinations(string, k):
        print(''.join(comb))
