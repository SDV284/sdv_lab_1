from math import sqrt

i = 100

while i > 0:
	for x in range(0,10):
		for y in range(0,10):
			print(round(sqrt(i), 2), end=" ")
			i-=1
		print("")
