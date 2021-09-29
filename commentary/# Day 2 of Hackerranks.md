# Day 2 of Hackerranks
I begin this day with search.  My target is another 5 chanllenges. I dont know if I will hit it.  There are a lot of things that need to be done.

## Problem 1:
Distinct triplets or Triple Sum
https://www.hackerrank.com/challenges/triple-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search
I thought of an elegant solution.  For each middle element in the triplet do a binary search for each element that could come before and after it given the criteria.  The binary search is index based and I could just count the number of elements that fall before that index.  The problem asks for distint triplets, however this would break down
when the elements are not distint.  I could make them distint though useing set and sorting them.  Just code it.

```python 3
    def triplets(a, b, c):
    b = list(sorted(set(b)))
    a = list(sorted(set(a)))
    c = list(sorted(set(c)))

    triplets = 0

    for center in b:
        left = 0
        right = len(a)
        midA = (left + right) // 2

        while left < midA:
            if a[midA] < center:
                left = midA
            elif a[midA] > center:
                right = midA
            else: 
                break
            midA = (left + right) // 2

        left = 0
        right = len(c)
        midC = (left + right) // 2

        while left < midC:
            if c[midC] < center:
                left = midC
            elif c[midC] > center:
                right = midC
            else:
                break
            midC = (left + right) // 2

        #print(f'for center {center}: indexes {midA} and {midC}')

        if a[midA] <= center:
            midA += 1
        if c[midC] <= center:
            midC += 1
        triplets += midA * midC

    return triplets
```
This worked on the first bug free attempt.  No real issues with this design.  The answers were correct and there were no speed issues the complexity of this one is O(b * (log(a) + log(c))) essentially O(n log(n)).  A good start indeed.

## Problem 2:
Minimum time required.  In the midst of a busy day I have thought about this problem.  Couldn't see it as a search problem.  Maybe a modulo math problem until I read the a post from the top commentor of the discussion thread attached to the problem.

It is a search problem.  A problem with bounded guesses for the number of days it will take for all of the machines to crank out the goal.  Guess the number of days.  See how much production there is in said days from all of the machines, change the guess accordingly.


