# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())

from collections import deque
q = deque()
maxx = deque()

for _ in range(N):
    cmd = list(map(int, input().split(' ')))
    if cmd[0] == 1:
        q.append(cmd[1])
        if len(maxx) == 0:
            maxx.appendleft(cmd[1])
        elif cmd[1] >= maxx[0]:
            maxx.appendleft(cmd[1])

    elif cmd[0] == 2:
        s = q.pop()
        if s == maxx[0]:
            maxx.popleft()

    elif cmd[0] == 3:
        print(maxx[0])
