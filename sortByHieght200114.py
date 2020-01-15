def sortByHeight(a):
    swapableIndexies = []
    for i, height in enumerate(a):
        if height != -1:
            swapableIndexies.append(i)
            
    swap = True
    if len(swapableIndexies) < 2:
        return a
    
    print(swapableIndexies)
    
    while swap:
        swap = False
        for j in range(1, len(swapableIndexies)):
            A = swapableIndexies[j - 1]
            B = swapableIndexies[j]
            if a[A] > a[B]:
                dummy = a[A]
                a[A] = a[B]
                a[B] = dummy
                swap = True
    
    return a
