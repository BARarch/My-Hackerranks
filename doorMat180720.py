size = list(map(int, input().split(' ')))
n = size[0]
m = size[1]

middle = n // 2
width = m
pattern = 1

for i in range(n):
    if i < middle:
        print(('.|.' * pattern).center(width, '-'))
        pattern += 2
    elif i == middle:
        print('WELCOME'.center(width, '-'))
    else:
        pattern -= 2
        print(('.|.' * pattern).center(width, '-'))
