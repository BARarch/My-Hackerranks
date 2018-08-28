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
