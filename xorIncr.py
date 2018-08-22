## xorIncr.py

## XOR Incrementation or Exclusive OR Icremetation

def bin_field(num, width=8):
	return bin(num)[2:].rjust(width, '0')

def last(lines, start=0):
	return start + lines * (lines - 1)


def test_line(start, length):
	xo = 0
	for i in range(start, start + length):
		xo ^= i
		print('  ^{} = {}'.format(str(i).ljust(8), bin_field(xo)))

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