class A:
    def show(self):
        print("Show from class A")

class B(A):
    def show(self):
        print("Show from class B")

class C(A):
    def show(self):
        print("Show from class C")

class D(B, C):
    pass

# Create an object of class D
d = D()

# Call the show() method on the D object
d.show()
