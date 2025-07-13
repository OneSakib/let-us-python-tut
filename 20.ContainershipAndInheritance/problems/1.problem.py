class Shape:
    pass


class Rectangle(Shape):
    pass


class Circle(Shape):
    pass


s=Shape()
c=Circle()
print(isinstance(s,Shape))
print(isinstance(s,Rectangle))
print(isinstance(s,Circle))
print(isinstance(Rectangle,Shape))
print(isinstance(Circle,Shape))
