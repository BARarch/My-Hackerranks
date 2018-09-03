N, X = list(map(int, input().split(' ')))

scores = []
for _ in range(X):
    scores += [list(map(float, input().split(' ')))]
    
for student in zip(*scores):
    print(sum(student) / len(student))
