#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
from itertools import repeat

# Complete the activityNotifications function below.
class ChargeChart:
    def __init__(self, size):
        self.chart = list(repeat(0, 201))
        self.size = size
        
    def add_charge(self, charge):
        self.chart[charge] += 1
        
    def remove_charge(self, charge):
        self.chart[charge] -= 1
        
    def get_median(self):
        counts = 0
        for amount in range(201):
            counts += self.chart[amount]
            if counts > (self.size // 2):
                return amount
            elif not(self.size % 2) and (counts == (self.size // 2)):
                for nextAmount in range(amount + 1, 201):
                    if nextAmount:
                        return (nextAmount + amount) / 2
            
            
            

def activityNotifications(expenditure, d):
    charges = ChargeChart(d)
    a = deque()
    note = 0
    
    for charge in expenditure:
        if len(a) < d:
            a.append(charge)
            charges.add_charge(charge)
        else:
            if charge >= (charges.get_median() * 2):
                note += 1
            a.append(charge)
            charges.add_charge(charge)
            charges.remove_charge(a.popleft())
    return note
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
