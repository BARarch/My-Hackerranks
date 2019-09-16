#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190913

import os
from cs_utils import *

def swap(string, pair):
	# 0 Based indexing
	a = pair[0] - 1
	b = pair[1] - 1
	if b < a:
		temp = a
		a = b
		b = temp

	#print("swap({}, {})".format(pair[0], pair[1]))
	return string[:a] + string[b] + string[a + 1:b] + string[a] + string[b + 1:]

def state(s):
	return s[0]

def last(s):
	return s[1]

def swapLexOrder(string, pairs):
	from collections import deque

	soln  = string
	states = {string: ''}
	q = deque([(string, ['start', ]), ])

	while q:
		s = q.pop()
		print('states {}, trys {}'.format(len(states), len(q)))
		for pair in pairs:
			#print(len(states))
			if pair != last(s):
				swaped = swap(state(s), pair)
				#print(swaped)
				if swaped not in states:
					states[swaped] = ''
					q.append((swaped, pair))
					if swaped > soln:
						soln = swaped

	return soln

def all_of_the_nodes(pairs):
	# Will need to pull out the pens for this one, Hehe
	

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    string = input()
    swaps = list_string_to_list(input())

    print("string: {}".format(string))
    print("swaps: {}".format(swaps))


    fptr.write(swapLexOrder(string, swaps))
    fptr.write('\n')

    fptr.close()
