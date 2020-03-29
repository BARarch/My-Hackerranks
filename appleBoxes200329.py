def additionWithoutCarrying(param1, param2):
    a = str(param1)
    b = str(param2)

    # Make equal lengths
    a = ('0' * (len(b) - len(a))) + a
    b = ('0' * (len(a) - len(b))) + b

    return int(''.join(map(lambda x: str(int(x[0]) + int(x[1]))[-1], zip(a, b))))
