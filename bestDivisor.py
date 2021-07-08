## Best Divisor

def get_factors(n):
    res = list(filter((lambda x: n % x == 0), range(1, n // 2 + 1)))
    res.append(n)
    return res

def digit_sum(n):
    return sum(map(int, [char for char in str(n)]))

if __name__ == "__main__":
    ## Single Input Enter Manually
    n = int(input("Single Input Enter Manually ").strip())
    #print(get_factors(n))

    maxSum = 0
    bestFactor = 1
    for fact in get_factors(n):
        ds = digit_sum(fact)
        print(ds)
        if ds > maxSum:
            maxSum = ds
            bestFactor = fact
        elif ds == maxSum and fact < bestFactor:
            bestFactor = fact

    print(bestFactor)

        



