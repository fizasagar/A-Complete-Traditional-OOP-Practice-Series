class Bank:
    # class variable
    bank_name = "Allied Bank"

    def __init__(self, customer_name):
        self.customer_name = customer_name

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"Customer: {self.customer_name}, Bank: {Bank.bank_name}")

# Creating objects
cust1 = Bank("Fiza")
cust2 = Bank("Warisha")

# Displaying before changing bank name
cust1.display()
cust2.display()

# Changing the bank name using class method
Bank.change_bank_name("Meezan Bank")

# Displaying after change
cust1.display()
cust2.display()
