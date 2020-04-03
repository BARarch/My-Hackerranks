def isSmooth(arr):
    if len(arr) % 2 == 1:
        middle = arr[len(arr) // 2]
    else:
        middle = arr[(len(arr) // 2) - 1] + arr[len(arr) // 2]

    return arr[0] == middle == arr[-1]


