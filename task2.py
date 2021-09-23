"""
    FirstCycleBufferClass - первый класс, реализующий циклический буфер
    Плюсы:
        - Простой в реализации, малое число методов
        - Длина буфера задается при создании объекта класса
        - Результат вывода объекта класса в строку - массив буфера
        - Новый элемент всегда добавляется в конец списка
        - Позволяет хранить в ячейках массивы
    Минусы:
        - Массив элементов добавляется в одну ячейку - нет возможности добавлять множестно
        элементов при одном запросе
        - нет возможности обращения по индексу
        - массив буфера имеет публичный уровень доступа, т.е. изменить элементы и получить массив
        можно не обращаясь к методам класса

    SecondCycleBufferClass - класс, реализующий циклический буфер
    Плюсы:
        - Результат вывода объекта класса в строку - массив буфера
        - Имеется возможность добавлять множество значений в буфер одним запросом,
        при этом троковые значения добавляются одним элементом
        - Имеется возможность получить индекс элемента при его добавлении
        - Имеется возможность получить последний элемент или элемент по индексу
        - Все переменные буфера имеют уровень доступа - привытный
    Минусы:
        - Фиксированная длина буфера
        - Нет возможности добавить в ячейку буфера массива
        - Нет обработки исключения при введении индекса, выходящего за пределы длины буфера



"""



class FirstCycleBufferClass:
    def __init__(self, length):
        self.buffer = []
        for i in range(length):
            self.buffer.append(0)

    def get_whole(self):
        return self.buffer

    def get_last(self):
        return self.buffer[-1]

    def put(self, value):
        self.buffer = self.buffer[1:] + [value]

    def __str__(self):
        return str(self.get_whole())


class SecondCycleBufferClass:

    def __init__(self):
        self.__buffer = []
        self.__index = 0
        for i in range(10):
            self.__buffer.append(0)

    def __str__(self):
        return str(self.get_whole())

    def get_whole(self):
        return self.__buffer

    def get_last_input(self):
        return self.__buffer[self.__index]

    def get_by_index(self, i):
        return self.__buffer[i]

    def put(self, value):

        if type(value) is list:
            for a in value:
                self.__index = self.__put_only_one(a)
        else:
            self.__put_only_one(value)
        return self.__index

    def __put_only_one(self, value):
        self.__index += 1
        if self.__index >= 10:
            self.__index = 0
        self.__buffer[self.__index] = value
        return self.__index


def check_first_class(value):
    buffer = FirstCycleBufferClass(value)
    buffer.put(4)
    buffer.put(12)
    print(buffer)
    buffer.put(5)
    print(buffer)
    print(buffer.get_last())
    buffer.put([4, 6, 10])
    print(buffer)
    print(buffer.get_last())


def check_second_class():
    buffer = SecondCycleBufferClass()
    print(buffer)
    buffer.put(9)
    buffer.put(1)
    print(buffer)
    print(buffer.get_last_input())
    index = buffer.put(2)
    buffer.put(10)
    print(buffer)
    print(buffer.get_by_index(index))
    buffer.put([1234, 234, 8, 9])
    print(buffer)
    index = buffer.put([18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
    print(buffer)
    print("Индекс последнего элемента:", index)
    buffer.put({'1': '2', '3': '4'})
    print(buffer)
    buffer.put("Строка")
    print(buffer)


check_first_class(8)
check_second_class()
