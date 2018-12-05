if __name__ == '__main__':
    mean1, mean2 = tuple(map(float, input().split(' ')))

    print(round(160 + (40 * (mean1 + (mean1 ** 2))), 3))
    print(round(128 + (40 * (mean2 + (mean2 ** 2))), 3))
