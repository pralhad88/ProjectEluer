# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 ?

count=1
while True:
	if (count%16==0) and (count%18==0) and (count%15==0) and (count%20==0) and(count%14==0) and (count%12==0) and(count%11==0) and (count%13==0) and (count%17==0) and(count%19==0):
		print(count)
		break 
	count+=1


smallest_num = 1
for i in range (1,21):
    if smallest_num % i > 0: # If the number is not divisible by i
        for k in range (1,21):
            if (smallest_num * k) % i == 0: # Find the smallest number divisible by i    
                smallest_num = smallest_num * k
                break
print (smallest_num)

