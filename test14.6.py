# def map_(func, some_list):
#     # some_list объект, над которым будет производиться преобразование
#     # func функция, которая должна выполняться над каждым объектом
#     outp = []
#     for i in range(len(some_list)):
#         outp.append(func(some_list[i]))
#     return outp
#
# C помощью метода строки str.lower переведите все элементы списка в нижний регистр.
#
# L = ['THIS', 'IS', 'LOWER', 'STRING']
# Ответ
# print(list(map(str.lower, L)))
# # ['this', 'is', 'lower', 'string']


# # Из заданного списка вывести только положительные элементы
# def positive(x):
#     return x > 0  # функция возвращает только True или False
#
# result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])
#
# # Возвращается итератор, т.е. перечисляйте или приводите к списку
# print(list(result))   # [1, 2]


# Отфильтруйте из заданного списка только четные элементы.
#
# [-2, -1, 0, 1, -3, 2, -3]
# Ответ
# def even(x):
#    return x % 2 == 0
#
# result = filter(even, [-2, -1, 0, 1, -3, 2, -3])
#
# print(list(result))   # [-2, 0, 2]


# # map + filter
# some_list = [i - 10 for i in range(20)]
# def pow2(x): return x**2
# def positive(x): return x > 0
#
# print(some_list)
# print(list(map(pow2, filter(positive, some_list))))
# Тоже самое через list comprehension:
#
# [i**2 for i in some_list if i > 0]


# map(func, list1)  # итератор, но никаких вычислений не будет произведено
# list(map(...))  # только здесь появляется объект
#
# [func(i) for i in list1]  # сразу готовый объект
#
#
# [func(i) for i in list1] == list(map(func, list1))  # результат один и тот же


# # Возвести первые 10 натуральных чисел в квадрат
# list(map(lambda x: x ** 2, range(1, 11)))  # правильно
# # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
# list(map(lambda x: x ** 2; x + 1, range(1, 11)))  #  неправильно, так как lambda содержит две конструкции


# d = {2 : "c", 1 : "d", 4 : "a", 3 : "b"}
#
# # Чтобы отсортировать его по ключам, нужно сделать так:
# print(dict(sorted(d.items())))
# # {1: 'd', 2: 'c', 3: 'b', 4: 'a'}

#sorted(d.items(), key=lambda x: x[1])  # сортировка по значению словаря


# есть список с данными о росте и весе людей. Задача — отсортировать
# их по индексу массы тела. Он вычисляется по формуле: рост в метрах возвести в квадрат,
# потом массу тела в килограммах разделить на полученную цифру.
# (вес, рост)
# data = [
#    (82, 191),
#    (68, 174),
#    (90, 189),
#    (73, 179),
#    (76, 184)
# ]
# print(sorted(data, key = lambda x: x[0] / x[1] ** 2))
#
# #Из списка в предыдущем задании найдите кортеж с минимальным индексом массы тела
#
# #Ответ
# print(min(data, key=lambda x: x[0] / x[1] ** 2))  # отбор по ключу





