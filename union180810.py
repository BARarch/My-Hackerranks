a = int(input())
engSet = set(list(map(int, input().split(' '))))
b = int(input())
frenchSet = set(list(map(int, input().split(' '))))

print(len(engSet.union(frenchSet)))
