K = int(input())
entries = list(map(int, input().split(' ')))
A = set(entries)
Good = set([])
Bad = set([])

for num in entries:
    if num in Good:
        # Move Num from Good to Bad
        Good.remove(num)
        Bad.add(num)      
    elif num in A:
        # Move Num from A to Good
        A.remove(num)
        Good.add(num)      
    # Terminate
    if (not bool(A)) and (len(Good) == 1):
        print(list(Good)[0])
        break
