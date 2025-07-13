class Progression:
    def __init__(self, start: int = 0):
        self._cur = start

    def __iter__(self):
        return self

    def advance(self):
        self._cur += 1

    def __next__(self):
        if self._cur is None:
            raise StopIteration
        else:
            data = self._cur
            self.advance()
            return data

    def display(self, n: int):
        print(' '.join(str(next(self)) for i in range(n)))


class AP(Progression):
    def __init__(self, start: int = 0, step: int = 1):
        super().__init__(start)
        self.__step = step

    def advance(self):
        self._cur += self.__step


class GP(Progression):
    def __init__(self, start: int = 1, step: int = 2):
        super().__init__(start)
        self.__step = step

    def advance(self):
        self._cur *= self.__step


class FP(Progression):
    def __init__(self, first: int = 0, second: int = 1):
        super().__init__(first)
        self.__prev = second-first

    def advance(self):
        self.__prev, self._cur = self._cur, self.__prev+self._cur


print("Default Progression")
p = Progression()
p.display(10)
print("Ap for step: 5")
a = AP(5)
a.display(10)
print("AP with  start 2 and step 4")
a = AP(2, 4)
a.display(10)
print("Print GP with default multiple")
a = GP()
a.display(10)
print("GP WIth start 1 and multiple 3")
a = GP(1, 3)
a.display(10)
print("Fibonacci series")
a = FP()
a.display(10)
print("FP With start values 4 and 6")
a = FP(4, 6)
a.display(10)
