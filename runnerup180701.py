if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    arr.reverse()
    topScore = arr[0]
    
    for a in arr:
        if a != topScore:
            print (a)
            break
