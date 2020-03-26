#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200326

def countNumbers(arr):
    res = []
    
    def countNumbersPair(pair):
        good = 0
        for i in map(str, range(pair[0], pair[1] + 1)):
            #print (i, end=" ")
            if len(i) == len(set(i)):
                good += 1
                #print("Good", end="")

        print(good)
        return good

    return list(map(countNumbersPair, arr))

if __name__ == '__main__':
    import os
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_rows = int(input().strip())
    arr_columns = int(input().strip())

    arr = []

    for _ in range(arr_rows):
        arr.append(list(map(int, input().rstrip().split())))

    result = countNumbers(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
