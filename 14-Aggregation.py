class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_employee_details(self):
        """Method to get employee details."""
        return f"Employee Name: {self.name}, Position: {self.position}"

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  # Aggregation: Department has reference to Employee

    def get_department_details(self):
        """Method to get department details."""
        return f"Department: {self.department_name}, {self.employee.get_employee_details()}"

# Creating an Employee object independently
employee1 = Employee("John Doe", "Software Engineer")

# Creating a Department object that stores reference to the Employee object
department1 = Department("IT Department", employee1)

# Displaying the details
print(department1.get_department_details())
