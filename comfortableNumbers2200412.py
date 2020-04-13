def comfortableNumbers(l, r):
    def upper(a):
        return a + sum(map(int, str(a)))

    def lower(a):
        return a - sum(map(int, str(a)))

    def test_b(a):
        def test(b):
            return a >= lower(b)
        return test

    H2 = {a: list(filter(test_b(a), range(a + 1, min(r + 1, upper(a) + 1)))) for a in range(l, r + 1)}

    return sum(map(len, H2.values()))

