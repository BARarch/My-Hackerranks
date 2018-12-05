from math import erf, sqrt

def cdf(x, u, o):
    ''' u: mean
        o: standard deviation
    '''
    return (1 / 2) * (1 + erf((x - u) / (o * sqrt(2))))

if __name__ == '__main__':
    mean, std = tuple(map(float, input().split(' ')))
    x1 = float(input())
    a2, b2 = tuple(map(float, input().split(' ')))

    ## Answer 1: less than x1
    print(round(cdf(x1, mean, std), 3))

    ## Answer 2: between a2 and b2
    print(round(cdf(b2, mean, std) - cdf(a2, mean, std), 3))
