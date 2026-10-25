class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def __str__(self):
        return f"Rectangle({self.width} x {self.height})"


for r in (Rectangle(4, 6), Rectangle(5, 5)):
    print(r)
    print("Area:", r.area())
    print("Perimeter:", r.perimeter())
    print("Square?", r.is_square())
