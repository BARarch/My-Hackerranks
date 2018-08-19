## sumset.py

## We are finding the greatest number for Camptain Bunny's
## Prison Tray Messaging Opporation

## The codes are numbers made from the single digits accross
## sequences of trays.  Valid Codes are numbers divisble by 3

## Our goal is to find the highest number that can be code given
## a set of trays

## Our solution exploits the mathematical proof that a number
## whos digits add up to a number that is divisible by 3, them
## that number is also divisible by three.

## This problem is 2 to the N complexity, the proposed solution
## focuses on optimal totals and reduces the complexity to linear
## in time, constant in memory

def number(summ, digits):
	return [summ, digits]
