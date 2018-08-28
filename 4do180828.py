def do_4(start):
	xor = 0
	res = []
	for i in range(start, start + 4):
		xor ^= i
		res.append(xor)
	return res
