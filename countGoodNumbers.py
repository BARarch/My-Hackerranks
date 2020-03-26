#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200326

def countNumbers(arr):

if __name__ == '__main__':
    arr_rows = int(input().strip())
    arr_columns = int(input().strip())

    arr = []

    for _ in range(arr_rows):
        arr.append(list(map(int, input().rstrip().split())))

    countNumbers(arr)
