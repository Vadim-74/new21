# #Сделаем функцию, которая будет выполнять принимаемую функцию дважды:
# def twice_func(inside_func):
#     """Функция, выполняющая дважды функцию принятую в качестве аргумента"""
#     inside_func()
#     inside_func()
#
#
# def hello():
#     print("Hello")
#
#
# test = twice_func(hello)
# print(test)
# # Hello
# # Hello


# #Сделаем функцию, которая будет возвращать функцию, всегда прибавляющую одно и тоже число x:
# def make_adder(x):
#    def adder(n):
#        return x + n # захват переменной "x" из nonlocal области
#    return adder  # возвращение функции в качестве результата
# #Тогда сделаем функцию, которая будет прибавлять число 5 к любому числу.
# # функция, которая будет к любому числу прибавлять пятёрку
# add_5 = make_adder(5)
# print(add_5(10))  # 15
# print(add_5(100))  # 105



# #Давайте посмотрим на примере, как добавить дополнительное поведение к основной функции.
# def my_decorator(a_function_to_decorate):
#     # Здесь мы определяем новую функцию - «обертку». Она нам нужна, чтобы выполнять
#     # каждый раз при вызове оригинальной функции, а не только один раз
#     def wrapper():
#         # здесь поместим код, который будет выполняться до вызова, потом вызов
#         # оригинальной функции, потом код после вызова
#         print("Я буду выполнен до основного вызова!")
#
#         result = a_function_to_decorate()  # не забываем вернуть значение исходной функции
#
#         print("Я буду выполнен после основного вызова!")
#         return result
#
#     return wrapper
# def my_function():
#    print("Я - оборачиваемая функция!")
#    return 0
#
# print(my_function())
# # Я - оборачиваемая функция!
# # 0
#
# decorated_function = my_decorator(my_function)  # декорирование функции
# print(decorated_function())
# # Я буду выполнен до основного вызова!
# # Я - оборачиваемая функция!
# # Я буду выполнен после основного вызова!
# # 0


# # Давайте попробуем замерить время выполнения системной функции для
# # возведения числа в степень 2 и соответствующего оператора.
# import time
#
# def decorator_time(fn):
#    def wrapper():
#        print(f"Запустилась функция {fn}")
#        t0 = time.time()
#        result = fn()
#        dt = time.time() - t0
#        print(f"Функция выполнилась. Время: {dt:.10f}")
#        return dt  # задекорированная функция будет возвращать время работы
#    return wrapper
#
#
# def pow_2():
#    return 10000000 ** 2
#
#
# def in_build_pow():
#    return pow(10000000, 2)
#
#
# pow_2 = decorator_time(pow_2)
# in_build_pow = decorator_time(in_build_pow)
#
# pow_2()
# # Запустилась функция <function pow_2 at 0x7f938401b158>
# # Функция выполнилась. Время: 0.0000011921
#
# in_build_pow()
# # Запустилась функция <function in_build_pow at 0x7f938401b620>
# # Функция выполнилась. Время: 0.0000021458


# # Возьмите из предыдущего примера декорированные функции, которые возвращают время работы
# # основной функции и найдите среднее время выполнения для 100 выполнений каждой функции.
# import time
#
# N = 100
#
#
# def decorator_time(fn):
#    def wrapper():
#        t0 = time.time()
#        result = fn()
#        dt = time.time() - t0
#        return dt
#    return wrapper
#
#
# def pow_2():
#    return 10000000 ** 2
#
#
# def in_build_pow():
#    return pow(10000000, 2)
#
#
# pow_2 = decorator_time(pow_2)
# in_build_pow = decorator_time(in_build_pow)
#
# mean_pow_2 = 0
# mean_in_build_pow = 0
# for _ in range(N):
#    mean_pow_2 += pow_2()
#    mean_in_build_pow += in_build_pow()
#
# print(f"Функция {pow_2} выполнялась {N} раз. Среднее время: {mean_pow_2 / N:.10f}")
# print(f"Функция {in_build_pow} выполнялась {N} раз. Среднее время: {mean_in_build_pow / 100:.10f}")

# # Имейте в виду, что при использовании синтаксического сахара,
# # на месте декорируемой функции появляется задекорированная функция!
# def my_decorator(fn):
#    def wrapper():
#        fn()
#    return wrapper  # возвращается задекорированная функция, которая заменяет исходную
#
# # выведем незадекорированную функцию
# def my_function():
#    pass
# print(my_function)  # <function my_function at 0x7f938401ba60>
#
# # выведем задекорированную функцию
# @my_decorator
# def my_function():
#    pass
# print(my_function)  # <function my_decorator.<locals>.wrapper at 0x7f93837059d8>



# # декоратор, в котором встроенная функция умеет принимать аргументы
# def do_it_twice(func):
#    def wrapper(*args, **kwargs):
#        func(*args, **kwargs)
#        func(*args, **kwargs)
#    return wrapper
#
# @do_it_twice
# def say_word(word):
#    print(word)
#
# say_word("Oo!!!")
# # Oo!!!
# # Oo!!!


# #Вот универсальный шаблон для декоратора:
# def my_decorator(fn):
#     print("Этот код будет выведен один раз в момент декорирования функции")
#     def wrapper(*args, **kwargs):
#         print('Этот код будет выполняться перед каждым вызовом функции')
#         result = fn(*args, **kwargs)
#         print('Этот код будет выполняться после каждого вызова функции')
#         return result
#     return wrapper


# Напишите декоратор, который будет подсчитывать количество
# вызовов декорируемой функции. Для хранения переменной, содержащей
# количество вызовов, используйте nonlocal область декоратора.
def counter(func):
   count = 0
   def wrapper(*args, **kwargs):
       nonlocal count
       func(*args, **kwargs)
       count += 1
       print(f"Функция {func} была вызвана {count} раз")
   return wrapper

@counter
def say_word(word):
   print(word)

say_word("Oo!!!")
# Oo!!!
# Функция <function say_word at 0x7f93836d47b8> была вызвана 1 раз

say_word("Oo!!!")
# Oo!!!
# Функция <function say_word at 0x7f93836d47b8> была вызвана 2 раз


# # Напишите декоратор, который будет сохранять результаты выполнения декорируемой
# # функции в словаре. Словарь должен находиться в nonlocal области в следующем формате:
# # по ключу располагается аргумент функции, по значению результат работы функции,
# # например, {n: f(n)}.
# #
# # И при повторном вызове функции будет брать значение из словаря,
# # а не вычислять заново. То есть словарь можно считать промежуточной памятью
# # на время работы программы, где будут храниться ранее вычисленные значения.
# # Исходная функция, которую нужно задекорировать имеет следующий вид и
# # выполняет простое умножение на число 123456789:
# # def f(n):
# #    return n * 123456789
# def cache(func):
#    cache_dict = {}
#    def wrapper(num):
#        nonlocal cache_dict
#        if num not in cache_dict:
#            cache_dict[num] = func(num)
#            print(f"Добавление результата в кэш: {cache_dict[num]}")
#        else:
#            print(f"Возвращение результата из кэша: {cache_dict[num]}")
#        print(f"Кэш {cache_dict}")
#        return cache_dict[num]
#    return wrapper

