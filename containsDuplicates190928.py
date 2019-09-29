def containsDuplicates(a):
    nums = {}
    for num in a:
        if num in nums:
            return True
        else:
            nums[num] = ''
    return False
        
