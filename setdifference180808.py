n = int(input())
a = set(list(map(int, input().split(' '))))
m = int(input())
b = set(list(map(int, input().split(' '))))

u = a.union(b)
i = a.intersection(b)

for num in i:
    u.discard(num)
    
print('\n'.join(map(str, sorted(list(u)))))
