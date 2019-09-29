def sumInRange(nums, queries):
    bigSum = [0 ,]
    for i, num in enumerate(nums):
        bigSum.append(bigSum[i] + num)

    res = 0
    for q in queries:
        res += bigSum[q[1] + 1] - bigSum[q[0]]
        
    return res % 1000000007
