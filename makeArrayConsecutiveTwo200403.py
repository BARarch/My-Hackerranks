def makeArrayConsecutive2(statues):
    last = sorted(statues)[0]
    needed = 0
    for i in list(sorted(statues))[1:]:
        needed += i - last - 1
        last = i

    return needed
