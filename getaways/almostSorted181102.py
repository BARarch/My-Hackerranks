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

	if not increasing:
		vals.append(n - 1)

	return (peaks, vals)

def swap_check(i, j ,arr):
	pass

def reverse_check(i, j, arr):
	pass
	

# Complete the almostSorted function below.
def almostSorted(arr):
	peaks, vals = peak_val(arr)

	## Uneven case
	if len(peaks) != len(vals):
		## There is some error with peaks and vals if this fires
		print('Uneven Case {} peaks and {} valleys'.format(str(len(peaks)), str(len(vals))))
		return 'no'

	## Too Many Peaks Case:
	## if there are more than 2 peaks array cannot be sorted in a single swap or reverse
	if len(peaks) > 2:
		return 'no'

	## Exactly One Peak and Exactly One Valley
	if len(peaks) == 1:
		peak = peaks[0]
		val = vals[0]

		## The one off swap case: the peak and valley are right next to each other
		if val - 1 == peak:
			pass

		## The reverse condition: there is space between the peak and the valley
		else:
			pass

	## Exactly Two Peaks and Two Valleys: the swap case
	if len(peaks) == 2
		pass
	return 'no'

if __name__ == '__main__':
	n = int(input())

	arr = list(map(int, input().rstrip().split()))

	almostSorted(arr)
