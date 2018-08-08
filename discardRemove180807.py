n = int(input())
s = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    cmd = input().split(' ')
    if len(cmd) == 1:
        ## This is a pop
        exec('s.{}()'.format(cmd[0]))
    else:
        ## This is remove / discard
        try:
            exec('s.{}(int({}))'.format(cmd[0], cmd[1]))
        except KeyError:
            pass

        
print(sum(list(s)))
