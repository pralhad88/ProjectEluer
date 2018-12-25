# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

sum=0
for number in range(1000):
	if (number%3==0) or (number%5==0): # remainder of number is 0 if you have divide with 3 or 5 then number will adding.
		sum+=number
print(sum)