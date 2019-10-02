def swap_sort(li):
    flag = True
    while flag:
        flag = False
        prev = None
        for i in range(1, len(li)):
            if prev is None:
                prev = li[0]
            if li[i] < prev:
                li[i - 1] = li[i]
                li[i] = prev
                flag = True
            else:
                prev = li[i]

    return li


from collections import deque
def merge_sort(li):
    if len(li) < 2:
        return li
    else:
        res = []
        left = deque(merge_sort(li[:len(li) // 2]))
        right = deque(merge_sort(li[len(li) // 2:]))

        while left and right:
            if left[0] < right[0]:
                res.append(left.popleft())
            else:
                res.append(right.popleft())
        while left:
            res.append(left.popleft())
		
        while right:
            res.append(right.popleft())

    return res

def in_place_merge_sort(li):
    return ipms_helper(li, 0, len(li))

def ipms_helper(li, start, end):
    if (end - start) == 1:
        return 
    else:
        mid = start + end // 2
        ipms_helper(li, start, mid)
        ipms_helper(li, mid, end)
        #mid = 1
        # [1,2,3] => [1,] [2, 3]
        left = start # loop to mid
        right = mid  # loop to end

        if left < mid and right < end:
            if li[left] < li[right]:
                left += 1
            else:
        


