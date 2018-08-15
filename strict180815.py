A = set(list(map(int, input().split(' '))))
n = int(input())
stopEarly = False
for _ in range(n):
    s = set(list(map(int, input().split(' '))))
    if len(s) >= len(A):
        stopEarly = True
        break
    elif s.difference(A):
        stopEarly = True
        break

print(not stopEarly)
