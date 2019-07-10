#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190709


import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    curr = head

    while curr is not None:
        # if value is less than or equal to curr we insert before
        if data < curr.data:
            if curr.prev is None:
                # This is the head
                insertedNode = DoublyLinkedListNode(data)
                curr.prev = insertedNode
                insertedNode.next = curr
                return insertedNode
            else:
                insertedNode = DoublyLinkedListNode(data)
                curr.prev.next = insertedNode
                insertedNode.next = curr
                insertedNode.prev = curr.prev
                curr.prev = insertedNode
                return head

        last = curr
        curr = curr.next
        

    ## End of list
    insertedNode = DoublyLinkedListNode(data)
    last.next = insertedNode
    insertedNode.prev = last

    return head
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
