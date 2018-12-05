from math import erf, sqrt

def cdf(x, u, o):
    ''' u: mean
        o: standard deviation
    '''
    return (1 / 2) * (1 + erf((x - u) / (o * sqrt(2))))

if __name__ == '__main__':
    mean, std = tuple(map(float, input().split(' ')))
    high = float(input())
    passed = float(input())

    ## Answer 1: Higher than 80
    print(round(100 * (1 - cdf(high, mean, std)), 2))

    ## Answer 2: Passed
    print(round(100 * (1 - cdf(passed, mean, std)), 2))

    ## Answer 3: Failed
    print(round(100 * (cdf(passed, mean, std)), 2))

