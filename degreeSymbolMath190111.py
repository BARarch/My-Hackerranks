from math import atan, degrees

ab = float(input().rstrip())
bc = float(input().rstrip())

print("{}".format(str(round(degrees(atan(ab / bc))))), end='')
print(u'\xb0')
