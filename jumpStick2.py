#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200419

def jumpStick(x, y):
    ## BFS with queue
    # Append right pop left
    from collections import deque
    runUntil = 6

    def hashResult(x, y, res):
        H[(x, y)] = res
        H[(x, -y)] = res
        H[(-x, y)] = res
        H[(-x, -y)] = res
        H[(y, x)] = res
        H[(y, -x)] = res
        H[(-y, x)] = res
        H[(-y, -x)] = res


    def jumpLength(i):
        # Start i from 1
        return 2 ** (i)

    def next_jump(jump):
        moves = jump[0]
        i = len(moves)
        x = jump[1][0]
        y = jump[1][1]
        Q.append((moves + 'N', (x, y + jumpLength(i))))
        Q.append((moves + 'S', (x, y - jumpLength(i))))
        Q.append((moves + 'E', (x + jumpLength(i), y)))
        Q.append((moves + 'W', (x - jumpLength(i), y)))

    #if (x, y) in H:
    #    print("Hashed")
    #    return H[(x, y)]

    Q = deque()

    ## All directions add to queue
    Q.append(('N', (0, 1)))
    Q.append(('S', (0, -1)))
    Q.append(('E', (1, 0)))
    Q.append(('W', (-1, 0)))

    j = ("", (0,0))
    next_jump(j)

    while len(j[0]) <= runUntil:
        j = Q.popleft()
        if j[1][0] == x and j[1][1] == y:
            hashResult(x, y, j[0])
            return j[0]
        next_jump(j)


        hashResult(x, y, "IMPOSSIBLE")
    return "IMPOSSIBLE"


if __name__ == '__main__':
    import os
    from cs_utils import *
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())
    H = {}

    for n in range(N):
        x, y = map(int, input().split(' '))
        print("Case #{}: {}".format(n + 1, jumpStick(x, y)))

    fptr.close()
