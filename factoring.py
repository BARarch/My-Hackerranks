
fact = lambda x : (lambda y : (x % y == 0))
factList = lambda z : list(filter(fact(z), list(range(1, 1 + z))))

def get_factors(x):
	return factList(x)

def valid_slice_size(string, ss):
	base = string[:ss]
	for i in range(ss, len(string), ss):
		if base != string[i : i + ss]:
			return False
	return True

def max_no_slices(string):
	for ss in get_factors(len(string)):
		if valid_slice_size(string, ss):
			return len(string) // ss

	return 1