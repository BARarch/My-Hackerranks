#!/bin/python3

import math
import os
import random
import re
import sys

class TestCase:
	def __init__(self, fileName):
		f = open(fileName, 'r')
		self.n = int(f.readline().rstrip())
		self.arr = list(map(int, f.readline().rstrip().split(' ')))

		f.close()

	def get_n(self):
		return self.n

	def get_arr(self):
		return self.arr

def peak_val(arr):
	peaks = []
	vals = []
	last = 0
	n = 1
	increasing = True
	for c in arr:
		#s = sorted(arr)
		if increasing:
			if c < last:
				peaks.append(n - 1)
				increasing = False
		else:
			if c > last:
				vals.append(n - 1)
				increasing = True
		last = c
		n += 1

	return (peaks, vals)
	

# Complete the almostSorted function below.
def almostSorted(arr):
	peaks, vals = peak_val(arr)

	return 'no'

if __name__ == '__main__':
	n = int(input())

	arr = list(map(int, input().rstrip().split()))

	almostSorted(arr)
