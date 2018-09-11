n = input()
s = input().split(' ') 
print(any(map(lambda x: x == ''.join(list(reversed(x))), s)) and all(map(lambda x: int(x) > 0, s)))
