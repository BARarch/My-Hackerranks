def magicalWell(a, b, n):
    from itertools import count
    A = count(a)
    B = count(b)
    money = 0
    for _ in range(n):
        money += next(A) * next(B)

    return money

