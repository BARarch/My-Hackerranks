from itertools import groupby

a = input()
reps = []

for k, g in groupby(a):
    reps.append((len(list(g)), int(k)))
    
print(' '.join(map(str, reps)))
