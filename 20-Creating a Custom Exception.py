# Step 1: Custom Exception
class InvalidAgeError(Exception):
    pass

# Step 2: Function that checks age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")
    else:
        print("Access granted!")

# Step 3: Using try...except to handle it
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("InvalidAgeError:", e)
except ValueError:
    print("Please enter a valid number.")
