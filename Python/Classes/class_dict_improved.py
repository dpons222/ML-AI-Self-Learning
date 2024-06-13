class Person:
    def __init__(self, first_name, last_name, age, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone = phone
        self.email = email

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Create Person objects and store them in the contacts dictionary
contacts = {}

contacts["Victor"] = Person("Victor", "Cortes", "57", "7872402276", "vcortes@gmail.com")
contacts["Cara"] = Person("Cara", "Bustin", "27", "123456789", "caras@email.com")
contacts["Aracelis"] = Person("Aracelis", "Nieves", "69", "7872401750", "dr.nieves21@gmail.com" )
contacts["Diego"] = Person("Diego", "Pons", "32", "7874221994", "dpons222@gmail.com")

# Function to get contact information
def get_contact_info(name):
    if name in contacts:
        return contacts[name]
    else:
        return None

# Example usage
contact_name = input("Enter name: ")
if get_contact_info(contact_name):
    person = contacts[contact_name]
    print(f"Contact information for {contact_name}:")
    print(f"First name: {person.first_name}")
    print(f"Last name: {person.last_name}")
    print(f"Phone: {person.phone}")
    print(f"Email: {person.email}")
else:
    print(f"No contact found for {contact_name}")
