n, m = tuple(map(int, input().rstrip().split(' ')))

N = list(map(int, input().rstrip().split(' ')))

freq = {}
for i in N:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

A = set(map(int, input().rstrip().split(' ')))
B = set(map(int, input().rstrip().split(' ')))

happyness = 0

for a in A:
    if a in freq:
        happyness += freq[a]

for b in B:
    if b in freq:
        happyness -= freq[b]

print(happyness)
