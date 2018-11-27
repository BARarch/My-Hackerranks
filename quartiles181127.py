#import numpy
#import scipy

def median(nums):
    if len(nums) % 2:
        ## List has an odd number of elements
        ## The median is the middle number
        return nums[len(nums) // 2]
    else:
        ## even number case
        ## average middle two
        return (nums[(len(nums) // 2) - 1] + nums[len(nums) // 2]) // 2

def separate(nums):
    if len(nums) % 2:
        ## List has an odd number of elements
        ## do not include the middle element
        ## ex: len(nums) = 5 
        ## lower = nums[:2]
        ## upper = nums[3:]
        return nums[:len(nums) // 2], nums[(len(nums) // 2) + 1:]
    else:
        ## List has an even number of elements
        ## even split
        return nums[:len(nums) // 2], nums[len(nums) // 2:]

N = int(input())
vals = list(sorted(map(int, input().split(' '))))
#print(vals)

Q2 = median(vals)
lower, upper = separate(vals)
Q1 = median(lower)
Q3 = median(upper)

print(Q1)
print(Q2)
print(Q3)
