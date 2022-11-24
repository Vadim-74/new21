
# # Создайте функцию-генератор, возвращающую
# # бесконечную последовательность натуральных чисел.
# def count(start=1, step=1):
#     counter = start
#     while True:
#         yield counter
#         counter += step

# # Создайте генератор цикла, то есть в функцию на входе будет передаваться
# # массив, например, [1, 2, 3],
# # генератор будет вечно работать возвращая 1 2 3 1 2 3… и так далее.
# def repeat_list(list_):
#    list_values = list_.copy()
#    while True:
#        value = list_values.pop(0)
#        list_values.append(value)
#        yield value
#
# for i in repeat_list([1, 2, 3]):
#    print(i)

#iter(int)  # TypeError: 'type' object is not iterable
#iter([1, 2, 3])  # <list_iterator at 0x7fb593ca1940>


# для примера возьмём строку
str_ = "my tst"
str_iter = iter(str_)

print(type(str_))  # строка
print(type(str_iter))  # итератор строки

# Получим первый элемент строки
print(next(str_iter))  # m

# Получим ещё несколько элементов последовательности
print(next(str_iter))  # y
print(next(str_iter))  #
print(next(str_iter))  # t
print(next(str_iter))  # s
print(next(str_iter))  # t