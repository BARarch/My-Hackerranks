from collections import Counter

n = int(input())
sizes = Counter(list(map(int, input().split(' '))))
m = int(input())
revenue = 0

for _ in range(m):
    cust = list(map(int, input().split(' ')))
    if cust[0] in sizes:
        revenue += cust[1]
        c = Counter({cust[0]: 1})
        sizes.subtract(c)
        if sizes[cust[0]] == 0:
            del sizes[cust[0]]

print(revenue)
