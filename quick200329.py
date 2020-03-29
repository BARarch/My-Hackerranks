def lineUp(commands):
    offsets = 0
    sameSide = 0
    for command in commands:
        if command == 'L' or command == 'R':
            offsets += 1
        if offsets % 2 == 0:
            sameSide += 1
            
    return sameSide


