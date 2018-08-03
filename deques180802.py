from collections import deque

d = deque()
N = int(input())

for _ in range(N):
    cmd = input().split(' ')
    if len(cmd) == 1:
        ## This is an output
        exec('d.{}()'.format(cmd[0]))
    else:
        ## This is an input
        exec('d.{}(str({}))'.format(cmd[0], cmd[1]))

print(' '.join(d))
