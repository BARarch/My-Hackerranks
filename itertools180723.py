A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))

print(' '.join(list(map(str, [(x, y) for x in A for y in B]))))
