# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

# First way to solve the problem

count = 0
number = 3
while True:
	s = 0
	for j in range(2,number):
		if number % j == 0:
			
	if s == 0:
		count+=1
		if count == 10001:
			print(number)
			break		
	number+=1

# Second way to solve the problem
def eratosthenes():
    D = {}  
    q = 2   
    while 1:
        if q not in D:
            yield q        
            D[q*q] = [q]   
        else:
            for p in D[q]: 
                D.setdefault(p+q,[]).append(p)
            del D[q]       
        q += 1

def nth_prime(n):
    for i, prime in enumerate(eratosthenes()):
        if i == n - 1:
            return prime

print(nth_prime(10001))

for i in range(1,10001):
	print(nth_prime(i))
