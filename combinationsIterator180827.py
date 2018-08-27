import itertools

n = input()
letters = input().split(' ')
k = int(input())

combs = itertools.combinations(letters, k)

count = 0
tot = 0
for comb in combs:
    if 'a' in comb:
        count += 1
    tot += 1
        
        
print(count / tot)
