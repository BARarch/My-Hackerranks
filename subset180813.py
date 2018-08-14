n = int(input())

for _ in range(n):
    a = int(input())
    A = set(list(map(int, input().split(' '))))
    b = int(input())
    B = set(list(map(int, input().split(' '))))
    
    print(not bool(A.difference(B)))
