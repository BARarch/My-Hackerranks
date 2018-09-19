class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

from collections import deque

def topView(root):
    tv = topView_h(root)
    #print(tv[0])
    print(' '.join(list(map(str, tv[1]))))
    
def topView_h(root):
    if root == None:
        return None
    
    ## PostOrder Transversal: Get Top Views for Children
    if root.left:
        leftTopView = topView_h(root.left)
        ## Adjust the pivot one to the right
        leftTopView[0] += 1
    else:
        leftTopView = None
    if root.right:
        rightTopView = topView_h(root.right)
        ## Adjust the pivot one to the left
        ## -- CAREFULL HERE --
        ## IF THE PIVOT IS ZERO AND YOU DECREMENT, THERE WILL BE PROBLEMS
        ## When the pivot is a negative number and the topview is divided
        ## you will get elements out of place for Bottom Left
        ## Likewise, for the other side if the left child top view
        ## has a piviot all the way to the right and the adjustment take place
        ## to move it one more to the right, this pivot is a key that is not on the 
        ## list, but since the division is a range, this does not throw an 
        ## exception and the correct results are generated

        # if rightTopView[0] > 0:
        rightTopView[0] -= 1
    else:
        rightTopView = None
    
    ## Start Current Top View
    result = [0, deque([root.info])]
    
    ## Divide up Top Views into top/bottom left/right Groups
    if leftTopView:
        leftTop = deque(list(leftTopView[1])[:leftTopView[0]])
        rightBottom = deque(list(leftTopView[1])[(leftTopView[0] + 1):])
    else:
        leftTop = None
        rightBottom = None
        
    if rightTopView:
        rightTop = deque(list(rightTopView[1])[(rightTopView[0] + 1):])
        leftBottom = deque(list(rightTopView[1])[:rightTopView[0]]) if rightTopView[0] >= 0 else deque([])
    else:
        rightTop = None
        leftBottom = None
    
    ## Pop into current top View left and right children
    ## on the left the left child is on top
    ## on the right the right child is on top
    ## for each loop for a given side a number is pop from the top and bottom
    ## if the top runs out of elements then we use the bottom
    
    ## On left side pop from right, append to left, increment pivot
    while leftTop or leftBottom:
        if leftTop:
            result[1].appendleft(leftTop.pop())
            if leftBottom:
                duh = leftBottom.pop()
        else:
            result[1].appendleft(leftBottom.pop())
        result[0] += 1
    
    ## On right side pop from left, append to right
    while rightTop or rightBottom:
        if rightTop:
            result[1].append(rightTop.popleft())
            if rightBottom:
                dope = rightBottom.popleft()
        else:
            result[1].append(rightBottom.popleft())
            
    return result

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)

