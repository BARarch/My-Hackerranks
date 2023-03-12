"""
This code is for LeetCode X

"""

## 3 Methods: They in my brain might as well produce them all.

## 1. Min on Left
def min_on_left(height):
    print('Doing min_on_left')
    def try_min_to_the_left(height):        
        res = 0
        for i, h in enumerate(height):      
            # Start at the other side
            # Find first element my height or taller
            j = len(height) - 1
            while (j - i) * h > res:
                if h <= height[j]:
                    res = (j - i) * h
                j -= 1 
        return res

    res = max((try_min_to_the_left(height), try_min_to_the_left(list(reversed(height)))))
    print(res)
    return res

## 1A. Min on Left with Memoization
def min_on_left_memoized(height):
    print('Doing min_on_left with Memoization')          
    res = 0
    min_on_right = {}
    for i, h in enumerate(height):      
        # Start at the other side
        # Find first element my height or taller
        j = len(height) - 1
        while (j - i) * h > res:
            #potential = (j - i) * h
            if h <= height[j]:
                res = (j - i) * h
            else:
                ## A min on right
                ## Although not optimal we still check
                if height[j] not in min_on_right:
                    temp_min_on_right = (j - i) * height[j]
                    min_on_right[height[j]] = temp_min_on_right
                    if temp_min_on_right > res:
                        res = temp_min_on_right
            j -= 1 
         
    print(res)
    return res

## 2. Min on Right: The moment method
def min_on_right(height):
    print('Doing min_on_right: linear moment method')
    resL = 0
    maxI = len(height) - 1
    # Find largest Left Moment
    for i, h in enumerate(height):
        if i * h >= resL:
            resL, maxI = i * h, i   # maxuimumIndex of maximum left Moment 

    resR = 0
    minJ = 0
    # Find largest Right Moment
    for j, h in enumerate(height):
        if (len(height) - j - 1) * h > resR:
            resR, minJ = (len(height) - j - 1) * h, j   # minimumIndex of maximum right moment

    print(f'containerBounds ({minJ},{maxI})')
    res = (maxI - minJ) * min([height[maxI], height[minJ]])
    
    print(res)
    return res
'''    def collect_left_moments(height):
        res = 0
        MomentMaxIndex = {i * h:i for i, h in enumerate(height)}
        #print(MomentMaxIndex)
        for moment in reversed(sorted(MomentMaxIndex.keys())):    # Geting all of the moments sorted largest first
            ## Remember this is min on right
            #print(f'Moment: {moment}')
            i, h, j = MomentMaxIndex[moment], height[MomentMaxIndex[moment]], 0
            while(j < i):
                if height[j] < h:
                    j += 1
                else:   
                    container = moment - (j * height[j])
                    #print(f'HasContainter {container}')
                    if container > res:
                        res = container
                    break               
        
        return res
    ## Repeat in other direction keep greatest result
    res = max((collect_left_moments(height), collect_left_moments(list(reversed(height)))))
    print(res)'''

 


## 3. Pour Water Find the largest puddle
def pour_water(height):
    print('Doing poured water')
    # This one should be fun 
    HeightIndecies = {}
    for i, h in enumerate(height):          # Indeies of heights are sorted for each entry
        if h in HeightIndecies:
            HeightIndecies[h].append(i)
        else:
            HeightIndecies[h] = [h, ]


    res = 0
    print(res)
    return res

def maxArea_original(self, height) -> int:
        currentlargestArea = 0
        N = len(height)
        for i, h in enumerate(height):
            if h * (N - 1) > currentlargestArea: ## There is a potiential maximum, do slice
                ## Where do I start in this slice
                ## Can I rule out elements too close based on current largerstArea
                startingOffset = (currentlargestArea // h) + 1 ## I will only try columns at least this far from me
                for j, h2 in enumerate(height[startingOffset + i:]):
                    if h2 >= h: ## New Largest Area
                        currentlargestArea = h * (j + 1)

        print(currentlargestArea)
        print("")                
        return currentlargestArea




class Solution:
    def maxArea(self, height) -> int:
        print()
        print(f"Testing {height}")
        MIN_ON_LEFT_RES, MEMO, MIN_ON_RIGHT_RES, POUR_WATER_RES  = [method(height) for method in [min_on_left, min_on_left_memoized, min_on_right, pour_water]]

        return MIN_ON_LEFT_RES

# Tester
def test_solution():
    PAPER_EXAMPLE_0 = [2,1,3,1]
    PAPER_EXAMPLE_1 = [1,1,1,1]
    PAPER_EXAMPLE_2 = [1,2,2,1]
    PAPER_EXAMPLE_3 = [1,6,6,1]

    solution = Solution()
    assert solution.maxArea([1,8,6,2,5,4,8,3,7]) == 49  ## Min on Right
    assert solution.maxArea([1,1]) == 1
    assert solution.maxArea(PAPER_EXAMPLE_0) == 4       ## Min on LEFT
    assert solution.maxArea(PAPER_EXAMPLE_1) == 3       ## Min on LEFT
    assert solution.maxArea(PAPER_EXAMPLE_2) == 3       ## Min on LEFT
    assert solution.maxArea(PAPER_EXAMPLE_3) == 6       ## Min on LEFT


if __name__ == "__main__":

    test_solution()