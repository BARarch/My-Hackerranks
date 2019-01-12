for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print( sum(map(lambda x: x[0] * x[1], zip(map(lambda y: 10 ** y, range((2 * i) - 1)), map(lambda z: i - abs(z), range(-i + 1, i))))) )
