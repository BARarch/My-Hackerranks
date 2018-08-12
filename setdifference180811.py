n = int(input())
engSet = set(list(map(int, input().split(' '))))
m = int(input())
frenchSet = set(list(map(int, input().split(' '))))

print(len(engSet.difference(frenchSet)))
