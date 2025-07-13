from abc import ABC, abstractmethod


class Printer(ABC):
    def __init__(self, name) -> None:
        self.__name = name

    @abstractmethod
    def print(self, docName):
        pass


class LaserPrinter(Printer):
    def __init__(self, name) -> None:
        super().__init__(name)

    def print(self, docName):
        print(">>>", 'LaserPrinter.print')
        print("Trying to print", docName)


class InkJetPrinter(Printer):
    def __init__(self, name) -> None:
        super().__init__(name)

    def print(self, docName):
        print("In Injket Printer")
        print("Truuing", docName)


p = LaserPrinter('Lasetjet  1100')
p.print('hello.pdf')
p = InkJetPrinter('IMB 2410')
p.print('hello.pdf')
