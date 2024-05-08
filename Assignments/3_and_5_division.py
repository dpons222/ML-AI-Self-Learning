#### find the sum of all numbers divisible by 3 or 5 below 100. Also, what they equal on each line####
numbers = range(1, 100)

sum = 0
#check if numbers divisble by 3 or 5 
for num in numbers :
    #iterating each number
    if num % 3 == 0 or num % 5 == 0:
        #keep a running sum
        sum += num
        #create empty list to later append 3 and 5
        divisor = []
        #append 3 to divisor list
        if num % 3 == 0 :
            divisor.append(3) 
        #append 5 to divisor list    
        if num % 5 == 0 :
            divisor.append(5)
        #checking to see if its only divisible by 3 or 5; not both    
        if len(divisor) == 1 :
            print(f"{num} divided by {divisor[0]} is {int(num / divisor[0])}")
        else :
             print(f"{num} divided by {divisor[0]} is {int(num / divisor[0])}; and {num} divided by {divisor[1]} is {int(num / divisor[1])}")  

print(sum)