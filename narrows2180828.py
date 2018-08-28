from itertools import combinations

def max_sum(l):
	digits = list(reversed(sorted(l)))

	for width in range(len(digits), 0, -1):
		for selection in combinations(digits, width):
			if (sum(selection) % 3) == 0:
				return int(''.join(map(str, list(selection))))

	return 0
