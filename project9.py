num=int(input())
for i in range(1,num):
	for j in range(1,num):
		a = i**2 + j**2
		for k in range(1,num):
			if a == k**2:
				if (i + j + k) == 1000:
					print(i*j*k)

x=1000
for a in range(1,x+1):
	for b in range(1,x+1):
		if a > b:
			continue
		if a + b + (a**2+ b**2) ** 0.5 == x:
			print(a,b, int((a**2+ b**2) ** 0.5))
			print(a * b * (int((a**2+ b**2) ** 0.5)))
