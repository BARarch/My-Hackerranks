def prob(a, b):
    return a / (a + b)

def probPercent(a):
    return a / 100

def fact(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * fact(n - 1)

def nChooseK(n, k):
    return fact(n) / (fact(k) * fact(n - k))

def binomialProb(x, n, p):
    return nChooseK(n, x) * (p ** (x)) * ((1 - p) ** (n - x))

if __name__ == "__main__":
    a, n = tuple(map(int, input().split(' ')))
    #print(a)
    #print(n)
    p = probPercent(a)

    ## CDF for no more than 2
    prob = 0.0
    if n <= 2:
        print(1.000)
    else:
        for x in range(3):
            prob += binomialProb(x, n, p)
        print(round(prob, 3))

    ## CDF for at least 2
    prob = 0.0
    if n < 2:
        print(0.000)
    else:
        for x in range(2, n + 1):
            prob += binomialProb(x, n, p)
        print(round(prob, 3))
