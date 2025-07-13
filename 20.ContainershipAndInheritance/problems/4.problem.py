from abc import ABC, abstractmethod


class Character(ABC):
    @abstractmethod
    def partriotism(self):
        pass


class Actor:
    def style(self):
        print("Actor style")


class Person(Actor, Character):
    def do_acting(self):
        print("Person do acring")

    def style(self):
        print("Person Style")

    def partriotism(self):
        print("Person haev partions")


p = Person()
p.partriotism()
p.style()
p.do_acting()

# c=Character()