class Date:
    def __init__(self, d, m, y) -> None:
        self.__day = d
        self.__mth = m
        self.__yr = y

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Date):
            return self.__day == value.__day and self.__mth == value.__mth and self.__yr == value.__yr
        return False
d1=Date(17,11,98)
d2=Date(17,11,98)
d3=Date(19,10,92)
print(d1==d2)
print(d1==d3)
print(d2==d3)

print(id(d1))
print(id(d2))
print(id(d3))