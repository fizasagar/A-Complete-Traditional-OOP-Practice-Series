class Product:
    def __init__(self, price):
        self._price = price  # private attribute

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price >= 0:
            self._price = new_price
        else:
            print("Price cannot be negative!")

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price


# Step-by-step testing
p = Product(100)

# 1. Show initial price
print("Initial Price:", p.price)   # Output: 100

# 2. Update price to 150
p.price = 150
print("Updated Price:", p.price)   # Output: 150

# 3. Try setting a negative price
p.price = -50                      # Output: Price cannot be negative!
print("After Invalid Update:", p.price)  # Output: 150

# 4. Delete the price
del p.price
