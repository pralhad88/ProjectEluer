count = 1
sum = 0
while True:
	for i in range(1,count+1):
		sum+=i

	total_divisor = 0
	for j in range(1,sum+1):
		if sum % j == 0:
			total_divisor+=1
	print (sum,total_divisor)
	sum = 0
	if total_divisor > 500:
		break
	total_divisor = 0
	count+=1