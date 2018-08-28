@time_this
def line_xor(start, length):
	littleXOR = 0
	for i in range(start, start + length):
		littleXOR ^= i

	return littleXOR
