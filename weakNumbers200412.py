def weakNumbers(n):
    def n_divisors(n):
        return len(list(filter(lambda x: n % x == 0, range(1, n // 2 + 1)))) + 1

    Divisors = [[], ]
    Divisors = {}
    Weakest = {}
    for num in range(1, n + 1):
        nDivs = n_divisors(num)
        if nDivs in Divisors:
            Divisors[nDivs].append(num)
        else:
            Divisors[nDivs] = [num, ]

        weakness = 0
        for c in filter(lambda x: x > nDivs, Divisors.keys()):
            weakness += len(Divisors[c])

        if weakness in Weakest:
            Weakest[weakness].append(num)

        else:
            Weakest[weakness] = [num, ]
            

    return [max(Weakest), len(Weakest[max(Weakest)])]
