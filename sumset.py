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

## Potential sequences of digits are expressed as numbers that 
## store not only the sequence of digits, sorted greatest, to 
## samllest to ensure teh highest possible code number, but
## also the sum of the digits

## For each digit in the input, tree numbers are kept to ensure 
## the optimal code

## the largest posible code whos sum of digits has a mod 3 of 0
## the largest posible code whos sum of digits has a mod 3 of 1
## and
## the largest posible code whos sum of digits has a mod 3 of 2

## the digit 0 has a mod 3 of 0 1 and 2!

class num:
	def __init__(self, _sum=None, code=None):
		self._sum = _sum
		self.code = code
		self.mod = _sum % 3

	def get_sum(self):
		return self._sum

	def get_code(self):
		return self.code

	def is_empty(self):
		return not bool(self._sum)

	def update(self, digit):
		if self.is_empty():
			return num(int(digit), digit) 
		else
			return num(self._sum + int(digit), digit + self.code)

	def __gt__(self, otherNum):
		return int(self.code) > int(otherNum.get_code())

def number(_sum, code):
	return [_sum, code]
