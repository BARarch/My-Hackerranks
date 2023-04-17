V = {}

def a():
    for i, j in zip(range(10), range(0,20,2)):
        V[i] = j

def b():
    for i, j in zip(range(10,20), range(0,40,2)):
        V[i] = j

if __name__ == "__main__":

    a()
    print(V)
    b()
    print(V)