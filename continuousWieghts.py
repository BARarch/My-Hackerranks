from typing import NewType


def newImbalanceBounds(wieghts):
    return max(wieghts), min(wieghts)

def getTotalImbalance(weight):
    from collections import deque
    # Write your code here
    contWeights = deque(weight)
    left = deque()
    right = deque()
    goleft = True
    maxx = max(contWeights)
    minn = min(contWeights)
    imbalanceTotal = maxx - minn

    while len(contWeights) > 1:
        if not goleft:
            while len(right) > 0:
                contWeights.append(right.popleft())
                left.append(contWeights.popleft())
                imbalanceTotal += newImbalanceBounds(contWeights)
            left.append(contWeights.popleft())             ## Pop to left one more time
            imbalanceTotal += newImbalanceBounds(contWeights)
            goleft = True

        else:
            while len(left) > 0:
                contWeights.appendleft(left.pop())
                right.appendleft(contWeights.pop())
                imbalanceTotal += newImbalanceBounds(contWeights)
            right.appendleft(contWeights.pop())             ## Pop to left one more time
            imbalanceTotal += newImbalanceBounds(contWeights)
            goleft = False

    return imbalanceTotal



                


