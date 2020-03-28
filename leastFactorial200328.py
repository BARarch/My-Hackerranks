def leastFactorial(n):
    def factorial():
        from itertools import count
        fact = 1
        c = count(1)
        while 1:
            fact *= next(c)
            yield fact

    F = factorial()
    f = 0
    while f < n:
        f = next(F)
    return f

    

