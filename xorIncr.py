## xorIncr.py

## XOR Incrementation or Exclusive OR Icremetation

from datetime import *

def bin_field(num, width=8):
	return bin(num)[2:].rjust(width, '0')

def last(lines, start=0):
	return start + lines * (lines - 1)


def test_line(start, length):
	xo = 0
	for i in range(start, start + length):
		xo ^= i
		print('  ^{} = {}'.format(str(i).ljust(8), bin_field(xo)))
	return xo


def time_this(process):
	def process_wrapper(*args, **kwargs):
		startTime = datetime.now()
		result = process(*args, **kwargs)
		print(str(datetime.now() - startTime))
		return result
	return process_wrapper

@time_this
def line_xor(start, length):
	littleXOR = 0
	for i in range(start, start + length):
		littleXOR ^= i

	return littleXOR

def do_4(start):
	xor = 0
	res = []
	for i in range(start, start + 4):
		xor ^= i
		res.append(xor)
	return res


def fast_line_xor(start, length):
	first4 = do_4(start)
	if start % 2:
		a = first4[0]
		b = first4[2]
		## Starting with odd number
		##	length	mod4:1	mod4:2	mod4:3	mod4:0
		## soln: [		a       a^x     b       b^x]
		## x = length + start
		if length % 4 == 1:
			return a
		elif length % 4 == 2:
			return a ^ (length + start - 1)
		elif length % 4 == 3:
			return b
		else:
			return b ^ (length + start - 1)
	else:
		a = first4[1]
		b = first4[3]
		## Starting with even number
		##	length	mod4:1	mod4:2	mod4:3	mod4:0
		## soln: [		b^x     a       a^x      b]
		## x = length + start
		if length % 4 == 1:
			return b ^ (length + start - 1)
		elif length % 4 == 2:
			return a
		elif length % 4 == 3:
			return a ^ (length + start - 1)
		else:
			return b

@time_this
## Perfectly Accurate Definition for Problem
def slow_xor(start, length):
	bigXOR = 0
	for i in range(length):
		littleXOR = 0
		startt = start + (i * length)
		#print(startt)
		for j in range(startt, (startt + length - i)):
			littleXOR ^= j
		bigXOR ^= littleXOR

	return bigXOR

@time_this
## Perfectly Accurate Definition for Problem
def fast_xor(start, length):
	bigXOR = 0
	for i in range(length):
		bigXOR ^= fast_line_xor(start + (i * length), length - i)

	return bigXOR