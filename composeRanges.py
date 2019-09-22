#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190922

def composeRanges(nums):
    if len(nums) == 0:
        return []
    prev = nums[0]
    rangeA = nums[0]
    ranges = []
    for n in nums[1:]:
        if n == prev + 1:
            prev = n
        else:
            if rangeA == prev:
                ranges.append(str(prev))
            else:
                ranges.append('->'.join((str(rangeA), str(prev))))
            rangeA = n
            prev = n

    if rangeA == prev:
        ranges.append(str(prev))
    else:
        ranges.append('->'.join((str(rangeA), str(prev))))

    return ranges

if __name__ == '__main__':
    import os
    from cs_utils import *
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nums = list_string_to_list(input())

    print("input: {}".format(nums))


    fptr.write(str(composeRanges(nums)))
    fptr.write('\n')

    fptr.close()
