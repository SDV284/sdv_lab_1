N = 0

while N < 1 or N > 9:
	N = int(input("Enter N:"))
	if N < 1 or N > 9:
		print("N must be between 1 and 9")
	else:
		break

i = N
while i > 0:
	j = 1
	while j < i or j == i:
		print(j, end=" ")
		j += 1
	print("")
	i -= 1