class Counter:
    # class variable to track object count
    count = 0

    def __init__(self):
        # increment count whenever a new object is created
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print(f"Total objects created: {cls.count}")

# Example usage
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
obj4 = Counter()

Counter.show_count()
