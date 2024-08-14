a, b = -1, -1

while a < 0 or a > 100 or b < 0 or b > 100:
	a = int(input("Enter a:"))
	if a < 0 or a > 100:
		print("\"a\" must be between 0 and 100")
	else:
		b = int(input("Enter b:"))
		if b < 0 or b > 100:
			print("\"b\" must be between 0 and 100")
		else:
			break

if a < b:
	X = b/a+1
elif a == b:
	X = 25
else:
	X = (pow(a,3)-5)/b

print("X is", X)