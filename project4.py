list1=[]
current = 0
for i in range(100,1000):
	for j in range(100,i):
		multi = str(i * j)
		multi1=int(multi)
		if multi == multi[::-1]:
			if multi1 > current:
				current = multi1
			list1.append(int(multi)) 
print(current)


max1=list1[0]
for k in list1:
	if k > max1:
		max1 = k
print(max1)