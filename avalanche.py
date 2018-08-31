## avalanche.py

## This is a scratch pad function library for the "Maximize it"
## Hackerrank Challenge.

## There are upto 7 list given were a number from each list is
## squared and sumed. The modulo of this sum is caluated.  We are
## to find the maximum modulo given the list of numbers and 
## modulo divisor.

## Itertools will be used to implement an Asemtotically Sound solution
## with out calculating 825,000 is modulos.

from itertools import *

def max_mod(lists, mod):
	modulos = list(repeat(0, mod))
	modulos[0] = 1

	for li in lists:
		newMods = list(repeat(0, mod))
		for mo in compress(count(0), modulos):	
			for i in li:
				newMods[(mo + ((i ** 2) % mod)) % mod] = 1
		modulos = newMods

	return list(compress(count(0), modulos))[-1]