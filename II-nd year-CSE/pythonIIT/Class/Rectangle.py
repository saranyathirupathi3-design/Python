class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rectangle1 = Rectangle(5, 3)  
rectangle2 = Rectangle(10, 4) 


print("Area of rectangle 1:", rectangle1.area())
print("Area of rectangle 2:", rectangle2.area())
