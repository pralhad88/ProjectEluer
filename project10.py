from math import ceil

# first way to solve
sum1 = 0
for i in range(2,2000000):
	s=0
	for j in range(2,i):
		if i % j == 0:
			s+=1
	if s == 0:
		sum1+=i
print(sum1)


# Second way to solve the question

def is_prime(num):
	top = int(ceil(num ** 0.5)) + 1
	for x in range(3, top, 2):
		if num % x == 0:
			return False
	return True

def primes(max=10):
	yield 2
	found = 1
	current = 3
	while current < max:
		if is_prime(current):
			yield current
			found+=1
		current+=2

print(sum(primes(2000000)))   