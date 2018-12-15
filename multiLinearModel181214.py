import numpy as np

if __name__ == '__main__':
    nF, nS = tuple(map(int, input().rstrip().split(' ')))
    x0 = []
    y0 = []
    for _ in range(nS):
        line = list(map(float, input().rstrip().split(' ')))
        x0.append([1, ] + line[:nF])
        y0.append(line[nF])

    X = np.matrix(x0)
    Y = np.matrix(y0).transpose()
    #print(np.matrix(x0))
    #print(np.matrix(y0).transpose())

    nT = int(input().rstrip())

    Xt = np.matrix([[1, ] + list(map(float, input().rstrip().split(' '))) for _ in range(nT)])
    #print(Xt)

    B = np.linalg.inv(X.transpose() * X) * X.transpose() * Y
    solns = Xt * B
    for row in np.nditer(solns):
        print(row)
