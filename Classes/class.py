class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
user_1 = Person("Diego", 32)
user_2 = Person("Cara" ,27)
user_3 = Person("Victor", 57)


greeting_method = user_3.greet  # No () at the end
print(greeting_method)  # Prints the method object