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
