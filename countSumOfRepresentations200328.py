def countSumOfTwoRepresentations2(n, l, r):
    sums = 0
    for i in range(l, r + 1):
        if i <= n - i and n - i <= r: # n - i in range(i, r + 1):
            sums += 1

    return sums


