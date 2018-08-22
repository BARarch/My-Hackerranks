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