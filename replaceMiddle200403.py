def replaceMiddle(arr):
    if len(arr) % 2 == 0:
        middle = arr[len(arr) // 2 - 1] + arr[len(arr) // 2]
        return arr[:len(arr) // 2 - 1] + [middle, ] + arr[len(arr) // 2 + 1:]
    else:
        return arr


