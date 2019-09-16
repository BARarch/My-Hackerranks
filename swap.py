def swap(string, pair):
	# 0 Based indexing
	a = pair[0] - 1
	b = pair[1] - 1
	if b < a:
		temp = a
		a = b
		b = temp

	#print("swap({}, {})".format(pair[0], pair[1]))
	return string[:a] + string[b] + string[a + 1:b] + string[a] + string[b + 1:]