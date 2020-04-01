def firstReverseTry(arr):
    if arr[-1:] == arr[:1]:
        return arr
    return arr[-1:] + arr[1:-1] + arr[:1]
