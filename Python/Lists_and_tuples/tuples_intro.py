#### Creating Tuples ####
#You create tuples by enclosing elements within parentheses ().
my_tuple = (1,2,3,4,5)

#Accessing Elements
#You can access elements of a tuple using index notation, just like with lists.
print(my_tuple[0])
print(my_tuple[2])
print("\n")


#Immutable nature - Once a tuple is created, you cannot modify its elements.
#example - my_tuple[0] = 10  # Error: TypeError: 'tuple' object does not support item assignment

#Tuple operations
#Slicing: Similar to lists, you can extract a portion of a tuple using slicing notation.
print(my_tuple[1:4])
print("\n")

#Concatenation: You can concatenate two tuples using the + operator.
another_tuple = (6,7,8)
combine_tuple = my_tuple + another_tuple
print(combine_tuple)
print("\n")

#Packing and Unpacking: You can pack and unpack tuples.
a, b, c = (1, 2, 3)
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
