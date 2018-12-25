Squar_sum = 0
Num_sum = 0
for i in range(1,101):
	Squar_sum = Squar_sum + (i**2)
	Num_sum = Num_sum + i

Answer = (Num_sum**2) - Squar_sum
print(Answer)
