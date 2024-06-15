#### Write a Python program that counts the number of even numbers in a given range and calculates their sum. #####

#create list of numbers 1 - 100
numbers = range(1, 101)

sum = 0 
count_even_numbers = 0
#count the number of even numbers
for num in numbers : 
    #check if number is even
    if num % 2 == 0 :
        #running count total of even numbers
        count_even_numbers += 1 
        #running sum total of even numbers
        sum += num
        #print sum for each iteration
        print(sum)
print(count_even_numbers)
print(sum)