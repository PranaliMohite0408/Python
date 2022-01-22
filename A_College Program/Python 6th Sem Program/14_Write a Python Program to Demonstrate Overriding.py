#write a python Prpgram to Demonstrate Overridinh....!

class Shape():
    def display(self):
        print("This is a Shape")

class Rectangle(Shape):
    def display(self):
        print("This is a Rectangle")
        super().display()

class Square(Rectangle):
    def display(self):
        print("This is Square")

sq=Square()
sq.display()
rect=Rectangle()
rect.display()
