[A[BN, M, P = tuple(map(int, input().strip().split(' ')))
rows = [N, M]
print(numpy.concatenate(tuple([list(map(int, input().strip().split(' '))) for _ in range(nm)] for nm in rows), axis=0))
