from collections import deque
n = int(input())
a = deque([])

for _ in range(n):
    comm = list(map(int, input().split(' ')))
    if comm[0] == 1:
        a.append(comm[1])
    elif comm[0] == 2:
        a.popleft()
    elif comm[0] == 3:
        print(a[0])
