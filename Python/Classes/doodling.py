class Student:
    """Creates the Student class, taking the first name, last name, and age parameters.
    It also creates an empty list for the student's grades."""
    minimum_passing_grade = 65  # The minimum passing grade for students

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grades = []

    def add_grade(self, score):
        """Adds a grade to the student's grades list."""
        self.grades.append(score)

    def is_passing(self):
        """Checks to see if the student is passing."""
        if not self.grades:
            return False
        avg_grade = sum(self.grades) / len(self.grades)
        return avg_grade >= self.minimum_passing_grade

    def get_average_grade(self):
        """Returns the average grade of the student."""
        if not self.grades:
            return None
        return sum(self.grades) / len(self.grades)

# Example usage
diego_pons = Student('Diego', 'Pons', 33)
diego_pons.add_grade(90)
diego_pons.add_grade(90)
diego_pons.add_grade(100)

# Print grades
print(diego_pons.grades)

# Check if the student is passing and print a message
if diego_pons.is_passing():
    avg_grade = diego_pons.get_average_grade()
    print(f'{diego_pons.first_name} is passing the class with an average grade of {avg_grade:.2f}')
else:
    print(f'{diego_pons.first_name} is not passing the class.')
