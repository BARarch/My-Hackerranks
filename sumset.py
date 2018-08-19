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
		if self.code:
			self.mod = _sum % 3
		else:
			self.mod = None

	def get_sum(self):
		return self._sum

	def get_code(self):
		return self.code

	def value(self):
		if self.is_empty():
			return 0
		return int(self.code)

	def is_empty(self):
		return self._sum is None

	def update(self, digit):
		digit = str(digit)
		if self.is_empty():
			return num(int(digit), digit) 
		else:
			return num(self._sum + int(digit), digit + self.code)

	def __gt__(self, otherNum):
		if self.is_empty():
			return False
		if otherNum.is_empty():
			return True
		if self.value() == otherNum.value():
			return len(self.code) > len(otherNum.get_code())
		return self.value() > otherNum.value()

	def greater(self, otherNum):
		if self > otherNum:
			return self
		else:
			return otherNum

	def __str__(self):
		return self.code

	def __repr__(self):
		if self.is_empty():
			return str([])
		return str([self._sum, self.code])

def number(_sum, code):
	return [_sum, code]

def sumset(L):
	digits = sorted(L)

	currSums = {}
	## These are mods
	currSums[0] = num()
	currSums[1] = num()
	currSums[2] = num()

	print(currSums)

	for d in digits:
		newSums = {}
		newSums[0] = num()
		newSums[1] = num()
		newSums[2] = num()
		if d == 0:
			## If the first digit is a update all mods
			newSums = {mod: currSums[mod].update(0) for mod in currSums}
		else:
			for mod in currSums:
				## Update all current sums
				## Save to a buffer
				exp = currSums[mod].update(d)
				newSums[exp.mod] = exp
		
		## Compare the sum with the same mod to the buffered number
		## Pass on the greater one
		currSums = {mod: currSums[mod].greater(newSums[mod]) for mod in currSums}
		print('d = {}'.format(str(d)))
		print(currSums)

	return currSums[0].value()








