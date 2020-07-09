#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190705


import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    merged = None
    curr1 = head1
    curr2 = head2

    if curr1.data < curr2.data:
        mergedHead = head1
        merged = curr1
        curr1 = curr1.next
    else:
        mergedHead = head2
        merged = curr2
        curr2 = curr2.next

    while curr1 is not None and curr2 is not None:
        if curr1.data < curr2.data:
            merged.next = curr1
            curr1 = curr1.next
        else:
            merged.next = curr2
            curr2 = curr2.next
        merged = merged.next

    if curr2 is None:
        merged.next = curr1
    elif curr1 is None:
        merged.next = curr2

    return mergedHead
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()
