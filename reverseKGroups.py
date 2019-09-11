#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190911
import os
from cs_utils import *

def reverseNodesInKGroups(l, k):
    def reversekNodes(l, end):
        curr = l
        prev = None
        while curr is not end:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        curr.next = prev
        
        return curr
    
    a = None
    b = l
    curr = l
    i = 0
    
    while curr is not None:   
        if (i % k) == 0:
            # goose
            if a is None:
                print("Goose None {}".format(curr.value))
                l = reversekNodes(b, curr)
                b.next = curr.next
                a = b
                b = curr.next
            else:
                print("Goose {}".format(curr.value))
                a.next = reversekNodes(b, curr)
                b.next = curr.next
                a = b
                b = curr.next
        
        if curr.next is None:
            print("Curr is None a element {}".format(i))
        curr = curr.next
        i += 1
        

    return l

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ll = list_string_to_linked_list(input())
    k = int(input()) 


    fptr.write(ll_to_string(reverseNodesInKGroups(ll, k)))
    fptr.write('\n')

    fptr.close()
