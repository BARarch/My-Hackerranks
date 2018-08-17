n = int(input())
A = set(list(map(int, input().split(' '))))

N = int(input())

for _ in range(N):
    cmd = input().split(' ')[0]
    exec('A.{}({})'.format(cmd, set(list(map(int, input().split(' '))))))
    
print(sum(A))
