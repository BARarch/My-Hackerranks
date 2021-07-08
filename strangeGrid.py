## The strange grid problem

def strangeGrid(r, c):
    if r % 2 == 0:
        ## Even row odd results
        return 10 * ((r - 1) // 2) + (c * 2) - 1
    else:
        return 10 * ((r - 1)// 2) + (c - 1) * 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    result = strangeGrid(r, c)

    fptr.write(str(result) + '\n')

    fptr.close()
