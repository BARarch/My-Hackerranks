# Day 1 Of Hackerranks
Count triplets looks like a pretty good problem.  At the moment I have no idea what this has to do with hashmaps and dictionaries.  We will see, lets make this one fun.
I had so many aproaches with this some.  Some incorrect, some overkill and incorrect, others slow.  One was correct and slow, another was fast and wrong in specfic edges cases.  The biggest thing I learned is to use the hints, don't take all weekend for a medium problem.  Move on, there is no need to be blue, learn something new!

# Day 3 Of Hackerranks
Today is going to be great.  Today is going to be straight forward.  Get the Cracking the codeing interview book ready.  Here we go.
## Problem 1:
Freqency Counts ay... I dusted of an old trick from TDI the coveted default dict.  Now this problem was a query integer type problem only the property that was checked was weather there was an integer with an exact frequency.  Return a 1 if there is an integer in the data structure whose frequency is exactly x.  The defaultdict came in hand when I could make a hash that maps all frequecies to elements in the data structure with that frequency.  The default value for any freuqency could be an empty set.

Now when I add or remove an element I could remove the element from the set of one frequency and add it to its updated frequency

adding an element:
            
            ```python 3
            if elm in numberToFreq:
                freqToNum[numberToFreq[elm]].remove(elm)
                numberToFreq[elm] += 1
                freqToNum[numberToFreq[elm]].add(elm)
            else:
                numberToFreq[elm] = 1
                freqToNum[1].add(elm)
            ```

removing and element:

            ```python 3
            if elm in numberToFreq:
                if numberToFreq[elm] > 1:
                    freqToNum[numberToFreq[elm]].remove(elm)
                    numberToFreq[elm] -= 1
                    freqToNum[numberToFreq[elm]].add(elm)
                else:
                    del numberToFreq[elm]
                    freqToNum[1].remove(elm)
            ```

## Problem 2:
Special Palantromic Strings again.  So for these strings I count the substrings that are inside that are considered special.  A sub string is special if it is unform
ie
    ssssss
or is uniform for every character except for the character in the middle
ie 
    bbsbb
Writing this solution was a case of one shot magic.  The program worked in accuracy and speed on the first design.

    ```python 3
    nSubstrings = 0
    for i, ch in enumerate(s):
        nSubstrings += 1
        
        prefix, j = ch, i + 1
        while j < n and s[j] == ch:
            nSubstrings += 1
            prefix += ch
            j += 1

        if s[j + 1: j + 1 + len(prefix)] == prefix:
            nSubstrings += 1
    ```

## Problem 3:
The common child.  I am hung up on an NP-Hard Problem.  Feeling like this is taking to long, I'm not smart enough.  This is how I learn.  This is actually a dynamic programing problem.  I didn't intend to do dynamic programming today and I will press on.  Mental fortitude will be the test and I will stick to what it is that I have
In the words of logic "I'd rather be hated for what I am than loved for what I'm not"

The solution when implemented as dynamic programming is eloquent and consise.  I had speed issues with some of the bigger cases.  The forum mentioned to switch to pypy.  It worked like a charm

    ```python 3
    def commonChild(s1, s2):
        currentRow = [0, ] * (len(s2) + 1)
        for letterR in s1:
            lastRow = currentRow
            currentRow = [0, ] * (len(s2) + 1)
            for i, letterC in enumerate(s2):
                if letterC == letterR:
                    currentRow[i + 1] = max(currentRow[i], lastRow[i + 1], lastRow[i] + 1)
                else:    
                    currentRow[i + 1] = max(currentRow[i], lastRow[i + 1])

        return currentRow[-1]
    ```

## Problem 4:
Unfairness.  This greedy algorithm looks sorta trivial.  Sort the list fill up a queue compute the minumium difference from computing the difference at each step.
I guess greed is good.  This one was a bit on the mindless side
```python 3
def maxMin(k, arr):
    from collections import deque
    kS = deque([])
    
    minUnfairness = max(arr)
    for num in sorted(arr):
        kS.append(num)
        if len(kS) > k:
            kS.popleft()
        if len(kS) == k:
            unfairness = kS[-1] - kS[0]
            if unfairness < minUnfairness:
                minUnfairness = unfairness

    return minUnfairness
```

## Problem 5:
Pairs
```python 3
    def pairs(k, arr):
```

I tried a naive pass on this one with a brute force 2D array that tries all pair
```python 3
    n = 0
    for i in arr:
        for j in arr:
            if j - i == k:
                n += 1

```
it was correct but slow for those big cases.
I implemented a binary search on a sorted array log(n).  This solution was nLog(n)
```python 3
    arr.sort()

    n = 0
    for num in arr:
        left = 0
        right = len(arr)
        #print(num)
        while left < right:
            
            mid = (right + left) // 2
            #print(f'mid = {mid}: {arr[mid]}')
            if (num - arr[mid] - k) == 0:
                n += 1
                break
            if (num - arr[mid] - k) < 0:
                right = mid
            elif left == mid:
                break
            else:
                left = mid

    return n 
```
we hit the target wit da turnup. Now it is time to chill.  Today was a good day.  I still have a long way to go to wendnesday, and Im down

