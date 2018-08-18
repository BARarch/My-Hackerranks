## solves the equasion 
## numerator = 2(d1 - dN_even + dN_odd)
## denominator = 1 if N is even and 3 if N is odd
## d is the distance between the Nth and Nth - 1 axil

def sproket(positions):
	last = 0
	numer = 0
	lastTermNeg = True
	for pos in positions:
		if last == 0:
			last = pos
		elif lastTermNeg:
			diff = pos - last
			numer += diff
			lastTermNeg = False
			last = pos
		else:
			diff = pos - last
			numer -= diff
			lastTermNeg = True
			last = pos

	if numer < 0:
		## Solution not possible
		return [-1, -1]
	elif lastTermNeg:
		return [2 * numer, 1]
	else:
		return [2 * numer, 3]

def get_numer(gear):
	return gear[0]

def get_denom(gear):
	return gear[1]

def show(n, numer, denom):
	print('gear {}: {}'.format(str(n), str([numer, denom])))

def showList(n, gear):
	print('gear {}: {}'.format(str(n), str(gear)))

def sproket_iter(n, positions, numer, lastNeg):
	if len(positions) <= 1:
		## Last Gear: Compute First and Last
		## rn = r1 / 2
		r1Numer = 2 * numer
		if lastNeg:
			r1Denom = 1
		else:
			r1Denom = 3

		print('First Gear: {}'.format(str([r1Numer, r1Denom])))
		if numer < r1Denom:
			return [-1, -1]
		else:
			return [numer, r1Denom]	

	elif lastNeg:
		## Compute Current Last term Negative
		## rn = dn - rn+1
		diff = positions[1] - positions[0]
		nextGear = sproket_iter(n + 1, positions[1:], numer + diff, False)
		showList(n + 1, nextGear)
		if get_numer(nextGear) == -1:
			return [-1, -1]
		_numer = (get_denom(nextGear) * diff) - get_numer(nextGear)
		_denom = get_denom(nextGear)
	else:
		## Comput Current Last term Positive
		## rn = dn - rn+1
		diff = positions[1] - positions[0]
		nextGear = sproket_iter(n + 1, positions[1:], numer - diff, True)
		showList(n + 1, nextGear)
		if get_numer(nextGear) == -1:
			return [-1, -1]
		_numer = (get_denom(nextGear) * diff) - get_numer(nextGear)
		_denom = get_denom(nextGear)

	if _numer < _denom:
		return [-1, -1]
	else:
		return [_numer, _denom]

def gears(positions):
	gearSize = sproket_iter(1, positions, 0, True)

	## Factor the result
	if (get_denom(gearSize) == 3) and ((get_numer(gearSize) % 3) == 0):
		return [get_numer(gearSize) // 3, 1]
	else:
		return gearSize





