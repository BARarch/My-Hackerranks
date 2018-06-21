class SolidSet:
	def __init__(self, A, B):
		if A <= B:
			self.lower = A
			self.upper = B
		else:
			self.lower = A
			self.upper = B

	def __len__(self):
		return self.upper - self.lower + 1

	def __add__(self, other):
		if self.lower <= other.lower and other.lower <= self.upper:
			if other.upper > self.upper:
				return SolidSet(self.lower, other.upper)
			else:
				return SolidSet(self.lower, self.upper)
		elif self.lower <= other.upper and other.upper <= self.upper:
			if other.lower < self.lower:
				return SolidSet(other.lower, self.upper)
			else:
				return SolidSet(self.lower, self.upper)
		elif self.lower > other.lower and self.upper < other.upper:
			return SolidSet(other.lower, other.upper)
		else:
			return

	def __str__(self):
		return '({}, {})'.format(str(self.lower), str(self.upper))

	def __repr__(self):
		return 'SolidSet({}, {})'.format(str(self.lower), str(self.upper))

def combine(unions, sset):
	## this function modifies the unionset in place
	startUnions = True
	while startUnions:
		startUnions = False
		for union in unions:
			tempUnion = sset + union
			if tempUnion:
				unions.remove(union)
				sset = tempUnion
				startUnions = True
				break

	unions.append(sset)
	return