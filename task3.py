"""
    Для для реалиции сортировки массива чисел был использован алгоритм сортировки слиянием.
    Данный алгоритм реализуется через рекурсию, из-за чего функций в реализации данного
    алгоритма две.
    Сложность алгоритма O(n log n), что уже указывает на высокую скорость выполнения.

    Однако, существующий алгоритм под названием "Быстрая сортировка" имеет большую скорость
    сортировки (в среднем в 2 раза выше сортировки слиянием) (при таком же показателе сложности O(n log n),
    не был выбран по причине, падения скорости выполнения (до сложности O(n^2)) при выборе
    в качестве начального элемента (т.е. от которого начнется сортировка)
    наименьшего или наибольшего. Т.о. в качестве стабильного метрода сортировки он не подходит.

    Были исключены алгоритмы сортировки методом "Всплывающего пузырька", "Выборки" и "Вставки" по причине
    сложности алгоритма O(n^2), что, очевидно, говорит о низкой скорости выполнения.

"""


def union(left, right):
    union_array = []
    left_i = 0  # индекс левой части
    right_i = 0  # индекс правой части

    for i in range(len(left) + len(right)):
        if left_i < len(left) and right_i < len(right):
            if left[left_i] <= right[right_i]:
                union_array.append(left[left_i])
                left_i += 1
            else:
                union_array.append(right[right_i])
                right_i += 1
        elif left_i == len(left):
            union_array.append(right[right_i])
            right_i += 1
        elif right_i == len(right):
            union_array.append(left[left_i])
            left_i += 1
    return union_array


def sort(array):
    if len(array) <= 1:
        return array
    middle = len(array) // 2  # средняя точка сортируемого массива
    part_l = sort(array[:middle])  # левая часть массива
    part_r = sort(array[middle:])  # правая часть массива
    united = union(part_l, part_r)
    return united


test_array = [12, 5, 18, 49, 90, 14, 0]
res_array = sort(test_array)
print(res_array)
