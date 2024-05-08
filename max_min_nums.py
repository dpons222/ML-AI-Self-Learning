import random


# Generate a list of 50 random numbers
random_numbers = [random.randint(1,1000000) for _ in range(50)]

print(max(random_numbers))
print(min(random_numbers))
