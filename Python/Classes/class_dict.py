class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
contacts = {}

contacts["Victor"] = {"phone": "7874221994", "email": "vcortes@gmail.com"}
contacts["Cara"] = {"phone": "123456789", "email": "caras@email.com"}


def get_contact_info(name):
    if name in contacts:
        return contacts[name]
    else:
        return None

contact_name = input("enter name here ")
if get_contact_info(contact_name):
    print(f"Contact information for {contact_name}:")
    print(f"Phone: {contacts[contact_name]['phone']}")
    print(f"Email: {contacts[contact_name]['email']}")
else:
    print(f"No contact found for {contact_name}")
    
