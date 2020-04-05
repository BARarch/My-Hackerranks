def isSumOfConsecutive2(n):
    from itertools import count
    from collections import deque
    nSums = 0
    consectutiveNumbers = deque()
    for consecutiveNumber in count(1):
        if consecutiveNumber == n:
            return nSums
        consectutiveNumbers.append(consecutiveNumber)
        if sum(consectutiveNumbers) == n:
            nSums += 1
        while sum(consectutiveNumbers) >= n:
            consectutiveNumbers.popleft()
            if sum(consectutiveNumbers) == n:
                nSums += 1

