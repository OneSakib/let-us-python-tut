class Base:
    def __method(self):
        print("In Base")

    def func(self):
        self.__method()


class Circle(Base):
    def __method(self):
        print("IN Derived Method")


b=Base()
b.func()
d=Circle()
d.func()