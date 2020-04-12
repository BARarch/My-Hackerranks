def squareDigitsSequence(a0):
    nums = set()
    a = a0
    n = 1
    while a not in nums:
        n += 1
        nums.add(a)
        a = sum(map(lambda x: x ** 2, map(int, str(a))))

    return n
