#Packing refers to the process of combining multiple values into a single tuple. This is done by placing the values separated by commas inside parentheses ().
my_tuple = 1, 2, 3
#In this example, 1, 2, and 3 are packed together into a tuple my_tuple. Python implicitly recognizes the comma-separated values as a tuple, even without explicitly using parentheses.


#Unpacking, on the other hand, is the process of extracting individual values from a tuple and assigning them to separate variables. This is particularly useful when you want to work with the elements of a tuple individually.
a,b,c = my_tuple
print(a)
print(b)
print(c)

#Multiple Return Values: Functions can return multiple values as a tuple, and you can then unpack these values when calling the function.

def get_coordinates():
    return 10, 20, 30

x, y, z = get_coordinates()
print(x)
print(y)
print(z)

#Swapping Variables: You can easily swap the values of two variables using tuple unpacking.
a,b = 1,2
b,a = a,b
print(a)
print(b)

#Iterating Over Tuples: Unpacking can simplify iterating over tuples in a loop.
coordinates = ((1,2), (3,4),(5,6))
for x, y in coordinates :
    print(f"X: {x} Y: {y}")

#### Arbitrary unpacking ####
#Python also supports arbitrary unpacking using the * operator. This allows you to collect multiple elements into a single variable, or to unpack the remaining elements of a tuple into a variable.

my_tuple = (1,2,3,4,5)
first, *rest = my_tuple


print(f"First: {first}")
print(f"Rest: {rest}")

#first, middle, last
my_tuple = (1,2,3,4,5)
first, *middle, last = my_tuple
print(f"First: {first}")
print(f"Middle: {middle}")
print(f"Last {last}")

#first,middle,second_last,last
my_tuple = (1,2,3,4,5)
first,*middle,second_last,last = my_tuple
print(f"First:{first}")
print(f"Middle: {middle}")
print(f"Second Last: {second_last}")
print(f"Last: {last}")