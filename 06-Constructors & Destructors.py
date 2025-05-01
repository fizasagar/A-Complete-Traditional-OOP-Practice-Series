class Logger:
    def __init__(self):
        print("Logger created! ✅")

    def __del__(self):
        print("Logger destroyed! ❌")

# Create object
log1 = Logger()

# Delete object manually (optional)
del log1

# Or wait for program end – destructor auto-call hota hai
