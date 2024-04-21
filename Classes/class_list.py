class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
user_1 = Person("Diego", 32)
user_2 = Person("Cara" ,27)
user_3 = Person("Victor", 57)

users =[user_1, user_2, user_3]

for user in users: 
    print(user.name)
    print(user.age)
    print(user.greet())