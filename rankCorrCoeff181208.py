def rank(x):
    sorts = sorted(x)
    return list(map(lambda i: sorts.index(i) + 1, x))

if __name__ == '__main__':
    n = int(input())

    X = list(map(float, input().rstrip().split(' ')))
    Y = list(map(float, input().rstrip().split(' ')))

    rankX = rank(X)
    rankY = rank(Y)

    rs = 1 - (6 * sum([(x - y) ** 2 for x, y in zip(rankX, rankY)]) / (n * (((n ** 2) - 1))))

    print(round(rs, 3))
