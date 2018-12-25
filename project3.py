# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

num= 600851475143
def factor(num):
	for i in range(3,num):
		s=0
		for j in range(2,i):
			if i%j==0:
				s+=1
		if s==0:
			if num % i == 0:
				print(i)
	
factor(num)
