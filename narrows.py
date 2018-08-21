## narrows.py

## We are finding the greatest number for Camptain Bunny's
## Prison Tray Messaging Opporation

## The codes are numbers made from the single digits accross
## sequences of trays.  Valid Codes are numbers divisble by 3

## Our goal is to find the highest number that can be code given
## a set of trays

## Our solution exploits the mathematical proof that a number
## whos digits add up to a number that is divisible by 3, them
## that number is also divisible by three.

from itertools import combinations

def max_sum(l):
	digits = list(reversed(sorted(l)))

	for width in range(len(digits), 0, -1):
		for selection in combinations(digits, width):
			if (sum(selection) % 3) == 0:
				return int(''.join(map(str, list(selection))))

	return 0