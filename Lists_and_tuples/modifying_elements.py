#### Modifying Elements:####

my_list = [1, 2, 3, 4, 5]

#Lists are mutable, so you can modify their elements directly.
my_list[0] = 10
print(f"1. Mutable list: {my_list}")  # Output: [10, 2, 3, 4, 5]

#Slicing: You can extract a portion of a list using slicing notation (up to but not including)
print(f"2. Slicing: {my_list[0:4]}")  # Output: [2, 3, 4]


#Concatenation: You can concatenate two lists using the + operator
another_list = [6, 7, 8]
combined_list = my_list + another_list
print(f"3. Concatenation: {combined_list}")  # Output: [10, 2, 3, 4, 5, 6, 7, 8]


#Appending: You can add elements to the end of a list using the append() method.
my_list.append(6)
print(f"4. Appending to list: {my_list}")


