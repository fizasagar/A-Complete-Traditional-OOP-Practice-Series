class Student:
    def __init__(self, name, marks):
        # using self to assign the values
        self.name = name
        self.marks = marks

    def display(self):
        # display student details
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

# Example usage
student1 = Student("Fiza", 92)
student1.display()
