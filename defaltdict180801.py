from collections import defaultdict
n, m = map(int, input().split(' '))
d = defaultdict(list)

for i in range(n):
    d[input()].append(str(i + 1))
    
for j in range(m):
    b = input()
    if b in d:
        print(' '.join(d[b]))
    else:
        print(str(-1))
