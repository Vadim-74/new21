# import random  # модуль, с помощью которого перемешиваем массив
#
# # пусть имеем массив всего лишь из 9 элементов
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
#
# is_sort = False  # станет True, если отсортирован
# count = 0  # счетчик количества перестановок
#
# while not is_sort:  # пока не отсортирован
#     count += 1  # прибавляем 1 к счётчику
#
#     random.shuffle(array)  # перемешиваем массив
#
#     # проверяем, отсортирован ли
#     is_sort = True
#     for i in range(len(array) - 1):
#         if array[i] > array[i + 1]:
#             is_sort = False
#             break
#
# print(array)
# # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(count)
# # 290698


array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
count = 0

# for i in range(len(array)):  # проходим по всему массиву
#     idx_min = i  # сохраняем индекс предположительно минимального элемента
#     for j in range(i, len(array)):
#         count += 1
#         if array[j] < array[idx_min]:
#             idx_min = j
#     if i != idx_min:  # если индекс не совпадает с минимальным, меняем
#         array[i], array[idx_min] = array[idx_min], array[i]

# # По убыванию
# for i in range(len(array)):
#     idx_max = i
#     for j in range(i, len(array)):
#         count += 1
#         if array[j] > array[idx_max]:
#             idx_max = j
#     if i != idx_max:
#         array[i], array[idx_max] = array[idx_max], array[i]

# # Пузырьковый
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
#
# for i in range(len(array)):
#     for j in range(len(array) - i - 1):
#         count += 1
#         if array[j] > array[j + 1]:
#             array[j], array[j + 1] = array[j + 1], array[j]
#
# print(array)
# print(count)


# # Вставками
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
# for i in range(1, len(array)):
#     x = array[i]
#     idx = i
#     while idx > 0 and array[idx-1] > x:
#         count += 1
#         array[idx] = array[idx-1]
#         idx -= 1
#     array[idx] = x
# print(array)
# print(count)

# Слияние
L = [2, 3, 1, 4, 6, 5, 9, 8, 7]
def merge_sort(L):  # "разделяй"
    if len(L) < 2:  # если кусок массива равен 2,
        return L[:]  # выходим из рекурсии
    else:
        middle = len(L) // 2  # ищем середину
        left = merge_sort(L[:middle])  # рекурсивно делим левую часть
        right = merge_sort(L[middle:])  # и правую
        return merge(left, right)  # выполняем слияние


def merge(left, right):  # "властвуй"
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result
print(merge_sort(L))

