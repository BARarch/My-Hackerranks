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

def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end='')

        node = node.next

        if node:
            print(sep, end='')

if __name__ == "__main__":
    print("Hello world")

##    N = int(input())
##    for _ in range(N): 
    llist = SinglyLinkedList()
    #n = int(input())
    
    rec =  map( llist.insert_node, map(int, input().split(" ")))
    print_singly_linked_list(llist.head, ", ")
        
