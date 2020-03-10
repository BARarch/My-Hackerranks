def isInfiniteProcess(a, b):
    if b >= a:
        return bool((a - b) % 2)
    else:
        return True


