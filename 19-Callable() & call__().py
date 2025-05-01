class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor

# Create an object of Multiplier with factor 3
m = Multiplier(3)

# Test using callable()
print("Is m callable?", callable(m))  # Output: True

# Call the object like a function
result = m(5)
print("m(5) =", result)  # Output: 15
