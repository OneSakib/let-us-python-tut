class Complex:
    def __init__(self, r=0.0, i=0.0):
        self.__real = r
        self.__imag = i

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Complex):
            return self.__real == value.__real and self.__imag == value.__imag
        return False


c1 = Complex(1.1, 0.2)
c2 = Complex(1.1, 0.2)
c3 = c2 == c1
print("SAME", c3)
