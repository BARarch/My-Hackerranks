#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190921

def houseRobber(nums):

    def houseRobberHelp(nums, n, HH):
        if n in HH:
            return HH[n]

        if len(nums) == 0:
            return 0

        if len(nums[n:]) == 1:
            HH[n] = nums[n]

        elif len(nums[n:]) == 2:
            HH[n] = max(nums[n:])


        elif len(nums[n:]) == 3:
            HH[n] = max(nums[n] + houseRobberHelp(nums, n + 2, HH), houseRobberHelp(nums, n + 1, HH))

        else:
            HH[n] = max(nums[n] + houseRobberHelp(nums, n + 2, HH), nums[n] + houseRobberHelp(nums, n + 3, HH), houseRobberHelp(nums, n + 1, HH)) 
            
        return HH[n]
        
    return houseRobberHelp(nums, 0, {})

if __name__ == '__main__':
    import os
    from cs_utils import *
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nums = list_string_to_list(input())

    print("input: {}".format(nums))


    fptr.write(str(houseRobber(nums)))
    fptr.write('\n')

    fptr.close()
