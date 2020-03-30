def rounders(n):
    rounded = 0
    res = []
    for i, c in enumerate(reversed(str(n))):
        print(c)
        digit = int(c) + rounded
        if digit >= 5:
            rounded = 1
        else:
            rounded = 0
        if i == len(str(n)) - 1:
            res.append(str(digit))
        else:
            res.append("0")

    return int(''.join(reversed(res)))
            
