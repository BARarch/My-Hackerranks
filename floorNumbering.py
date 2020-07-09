#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200326

# Complete the getLuckyFloorNumber function below.
def getLuckyFloorNumber(n):
    def luckyFloorNumber():
        floor = 0
        while True:
            floor += 1
            if '4' in str(floor) or '13' in str(floor):
                continue
            yield floor

    floors = luckyFloorNumber()
    for _ in range(n):
        luckyFloor = next(floors)

    return luckyFloor
    

if __name__ == '__main__':
    import os
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    res = getLuckyFloorNumber(n)

    fptr.write(str(res) + '\n')

    fptr.close()
