class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # calling Person's constructor
        self.subject = subject

    def display(self):
        print("Teacher name:", self.name)
        print("Subject:", self.subject)

# Create Teacher object
t1 = Teacher("Fiza", "Computer Science")
t1.display()
