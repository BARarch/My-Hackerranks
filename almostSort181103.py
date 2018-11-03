def peak_val(arr):
	peaks = []
	vals = []
	last = 0
	n = 1
	increasing = True
	for c in arr:
		#s = sorted(arr)
		if increasing:
			if c < last:
				peaks.append(n - 1)
				increasing = False
		else:
			if c > last:
				vals.append(n - 1)
				increasing = True
		last = c
		n += 1

	if not increasing:
		vals.append(n - 1)

	return (peaks, vals)

def swap_check(i, j ,arr):
	## i: the first peak
	## j: the second valley 
	I = i - 1
	J = j - 1

	if arr[J] < arr[I + 1] and arr[I] > arr[J - 1]:
		print('yes')
		print('swap {} {}'.format(str(i), str(j)))
	else:
		print('no')

	return


def reverse_check(i, j, arr):
	I = i - 1
	J = j - 1

	fore = arr[:I]
	aft = arr[J + 1:]

	if fore and fore[-1] > arr[J]:
		print('no')
		return
	if aft and aft[0] < arr[I]:
		print('no')
		return

	print('yes')
	print('reverse {} {}'.format(str(i), str(j)))
	return

def swap_check_one_off(i, j, arr):
	## This swap check, checks the swaps against the elements on the 
	## outside of the swap range
	I = i - 1
	J = j - 1

	fore = arr[:I]
	aft = arr[J + 1:]

	if fore and fore[-1] > arr[J]:
		print('no')
		return
	if aft and aft[0] < arr[I]:
		print('no')
		return

	print('yes')
	print('swap {} {}'.format(str(i), str(j)))
	return

# Complete the almostSorted function below.
def almostSorted(arr):
	peaks, vals = peak_val(arr)
	print('peaks:', end=' ')
	print(peaks)
	print('valleys:', end= ' ')
	print(vals)

	## Uneven case
	if len(peaks) != len(vals):
		## There is some error with peaks and vals if this fires
		print('Uneven Case {} peaks and {} valleys'.format(str(len(peaks)), str(len(vals))))
		print('no')
		return

	## Too Many Peaks Case:
	## if there are more than 2 peaks array cannot be sorted in a single swap or reverse
	if len(peaks) > 2:
		print('no')
		return

	## Exactly One Peak and Exactly One Valley
	if len(peaks) == 1:
		peak = peaks[0]
		val = vals[0]

		## The one off swap case: the peak and valley are right next to each other
		if (val - 1) == peak:
			swap_check_one_off(peak, val, arr)

		## The reverse condition: there is space between the peak and the valley
		else:
			reverse_check(peak, val, arr)
		return

	## Exactly Two Peaks and Two Valleys: the swap case
	if len(peaks) == 2:
		p1, p2 = peaks
		v1, v2 = vals

		## Both Peak valley pairs must be one off
		if (v1 - 1) == p1 and (v2 - 1) == p2:
			swap_check(p1, v2, arr)
		else:
			print('no')
		return


if __name__ == '__main__':
	n = int(input())

	arr = list(map(int, input().rstrip().split()))

	almostSorted(arr)
