"""
This code is for LeetCode X

"""

import qtimer


def print_and_assign(x):
    ''' Prints to stdio and returns value
        '''
    ''' I can display intermediate results for solution when they are done 
        instead of waiting for all of them.  I can get fast reslts without 
        printing the results before returning when I do asolutiuon function for
        one of those index scounting problems 
        '''
    ''' res = max((try_min_to_the_left(height), try_min_to_the_left(list(reversed(height)))))
        return res

        BECOMES

        return max((try_min_to_the_left(height), try_min_to_the_left(list(reversed(height))))) 
        
        '''
    print(x, end="\n")
    return x

## 3 Methods: They in my brain might as well produce them all.

## 1. Min on Left
#@qtimer.timeit
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
    
    return max((try_min_to_the_left(height), try_min_to_the_left(list(reversed(height)))))

## 1A. Min on Left with Memoization
## !! This one passes on LeetCode it is fast enough !!
#@qtimer.timeit
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
         
    
    return res

## 2. Min on Right: The moment method
#@qtimer.timeit
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
    return (maxI - minJ) * min([height[maxI], height[minJ]])
    
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
#@qtimer.timeit
def pour_water(height):
    print('Doing poured water')
    # This one should be fun 
    ''' The guiding principle here is 
        if there is a container of height h, 
        there shall only be one
        
        I can start with the tallest two walls heights (hTallest and hSecondTallest).
        The resulting container will be of height hSecondTallest.
        I keep the bounds (leftMostContaiWall, rightMostContainerWall) to find the largest containers for each height.
        
        Iterate from the tallest to shortest wall '''

    def generate_tallest(height):
        ''' Create iterator that returns each wall hieght and thier index in a sequence
            from the tallest to the shortest '''

        from collections import defaultdict
        HeightIndecies = defaultdict(lambda : [])
        for i, h in enumerate(height):          # Indeies of heights are sorted for each height key
            HeightIndecies[h].append(i)

        for h in reversed(sorted(height)):
            yield HeightIndecies[h].pop(), h
    
    ''' Start Here '''
    tallest = generate_tallest(height)
    leftMostContainerWall, h = next(tallest)
    rightMostContainerWall = leftMostContainerWall
    res = 0

    ''' Here Goes GODSPEED! '''
    for i, h in tallest:
        if h * (len(height) - 1) < res:
            print(f'Stopped Short {h} wall hieght')        
            return res
        if i > rightMostContainerWall:
            ## New Container if i is to the right of the right most container wall at this point
            rightMostContainerWall = i
            container = h * (i - leftMostContainerWall)
        elif i < leftMostContainerWall:
            ## New Container if i is to the left of the left most container wall at this point
            leftMostContainerWall = i
            container = h * (rightMostContainerWall - i)
        
        if container > res:
            res = container

        ''' Solution is accurate with Nlog(N) time complexity Beats 90% in time and 95 in Memory
            '''
    return res

#@qtimer.timeit
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

## 4. The Fastest Algorithm: Check from the ends move in
#@qtimer.timeit
def ends_first(height) -> int:
    ''' This is the fastest algorithm I found on leetCode.  
        I will implement it here. It has the same geometrical principle as my poured water
        algrothm, in that there is only one maximal area container for a container of height h. 
        Except we do a greedy search starting with the widest containers instead of the tallest. 
        This does not require an NlogN search and is a liner algorithm.'''

    print("Doing ends first")
    res = 0

    left, right = 0, len(height) - 1

    while left < right:
        #print(f'trying postions ({left}, {right})')
        hLeft, hRight = height[left], height[right]
        containerSize = min(hLeft, hRight) * (right - left)
        if containerSize > res:
            res = containerSize

        if hLeft < hRight:
            # Find a larger container by finding a higher left wall by checking to the right
            i = left
            while height[i] <= hLeft and i < right:
                i += 1
            left = i
        else:
            j = right
            # Find a larger container by finding a higher right wall by checking to the left
            while height[j] <= hRight and j > left:
                j -= 1
            right = j
 
    return res

class Solution:
    def maxArea(height) -> int:
        #print(f"Testing {height}")
        return print_and_assign(min_on_left(height))

    @classmethod
    def test_cases(cls):
        assert cls.maxArea([1,8,6,2,5,4,8,3,7]) == 49  ## Min on Right
        yield
        assert cls.maxArea([1,1]) == 1
        yield
        assert cls.maxArea([2,1,3,1]) == 4       ## Min on LEFT
        yield
        assert cls.maxArea([1,1,1,1]) == 3       ## Min on LEFT
        yield
        assert cls.maxArea([1,2,2,1]) == 3       ## Min on LEFT
        yield
        assert cls.maxArea([1,6,6,1]) == 6
        yield       ## Min on LEFT``


class MEMO(Solution):    
    def maxArea(height) -> int:
        return print_and_assign(min_on_left_memoized(height))

class MIN_ON_RIGHT_RES(Solution):    
    def maxArea(height) -> int:
        return print_and_assign(min_on_right(height))

class POUR_WATER_RES(Solution):    
    def maxArea(height) -> int:
        return print_and_assign(pour_water(height))

class ENDS_RES(Solution):    
    def maxArea(height) -> int:
        return print_and_assign(ends_first(height))
   

def compose_tests(cls):
    return cls.test_cases()

# Tester
def test_solution():
    ## Run Tests, set timers, compare answers with this class
    #Solutions = [Solution, MEMO, MIN_ON_RIGHT_RES, POUR_WATER_RES, ENDS_RES]
    Solutions = [Solution, MEMO, POUR_WATER_RES, ENDS_RES]
    
    ### [min_on_left, min_on_left_memoized, min_on_right, pour_water, ends_first]

    

    cases2 = list()
    
    print(len(Solutions))
    ## Finish all testcases per solution
    for soln in Solutions:
        for case in soln.test_cases():
            print('passed')
        print()

    ## Zip them together to compare results
    for _ in zip(*[soln.test_cases() for soln in Solutions]):
        print('passed')
        print()

    




    


if __name__ == "__main__":

    test_solution()