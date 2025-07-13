class Fruit:
    count = 0

    def __init__(self, name='', size='', color=''):
        Fruit.count += 1
        self.__name = name
        self.__size = size
        self.__color = color

    def display(self):
        return {'name': self.__name, 'size': self.__size, 'color': self.__size, 'count': Fruit.count}


f1 = Fruit('Banana', 'sdd', 'sdfdf')
f2 = Fruit('dfg', 'sdd', 'sdfdf')
f3 = Fruit('Bandsfgana', 'sdd', 'sdfdf')
f4 = Fruit('sdf', 'sdd', 'sdfdf')
print(Fruit.count)

print(f1.display())
print(f4.display())
