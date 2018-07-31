from itertools import permutations

z = input().split(' ')
k = int(z[1])
string = sorted(z[0])

for perm in permutations(string, k):
    print(''.join(perm))
