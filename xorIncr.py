## xorIncr.py

## XOR Incrementation or Exclusive OR Icremetation

def bin_field(num, width=8):
	return bin(num)[2:].rjust(width, '0')

def last(lines, start=0):
	return start + lines * (lines - 1)
