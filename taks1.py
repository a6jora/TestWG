"""
    def is_even() - решение по поиску четности числа основано на битовых операциях,
                    в частности побитовом "И"
    Плюсы:
        - скорость выполнения операции булевого умножения выше в разы
        в сравнении с операцией "остаток от деления"
        - отсутствует операция сравнения, что так же увеличивает скорость выполнения
    Минусы:
        - требуется инверсия результата вычисления
        - коретно работает только со степенями 2, что не дает возможности
        изменить функцию на проверку кратности другим числам при простой замене числа
        - для неподготовленного пользователя значение 1, как 2^0, не является очевидным.
        (0 указывает на номер разряда)


    def is_even_default() - решение по поиску четности числа, представленное
                            в тестовом задании (дано по умолчанию)
    Плюсы:
        - алгоритм универсален для нахождения кратности числа для любого
        - по коду, очевидно кратность какому числу проверяется
    Минусы:
        - операция "остаток от деления" имеет низкую скорость, по сравнению
        с побитовым "И"
        - операция сравнения результата снижает скорость выполнения функции
"""


def is_even(value):
    return not value & 1


def is_even_default(value):
    return value % 2 == 0


def check():
    a = 23423429345
    b = 812642345452
    print(is_even(a), is_even(b), sep='~~~')
    print(is_even_default(a), is_even_default(b), sep='~~~')


check()