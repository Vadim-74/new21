# def hello_world():
#    result = "Hello World"
#    print(result)
#
# hello_world()

#

# def pow_func(a=4, n=2):
#    if a % n == 0:
#       print(n)
#
# pow_func()  # 9
# pow_func(8, 5)  # 125

# def reverse_stair(n):
#    for i in range(n, 0, -1):
#        print("*" * i)
#
# reverse_stair(8)

# def get_multipliers(a):
#    count = 0
#    for n in range(1, a + 1):
#        if a % n == 0:
#            count += 1
#
#    return count
#
# print(get_multipliers(5))  # 2
# print(get_multipliers(4))  # 3

# def check_palindrome(str_):
#    str_ = str_.lower()
#    str_ = str_.replace(" ", "")
#
#    if str_ == str_[::-1]:
#        return True
#    else:
#        return False
#
# print(check_palindrome("test"))  # False
# print(check_palindrome("Кит на море не романтик"))  # True

# def get_my_func():
#    def hello_world():
#        print("Hello")
#    return hello_world
#
# hello_world_func = get_my_func()  # получить функцию в качестве результата
#
# print(type(hello_world_func))  # <class 'function'>
# hello_world_func()  # Hello

# def get_mul_func(m):
#    nonlocal_m = m
#
#    def local_mul(n):
#       return n * nonlocal_m
#
#    return local_mul
#
#
# two_mul = get_mul_func(2)  # возвращаем функцию, которая будет умножать числа на 2
# print(two_mul(5))  # 5 * 2

# a = [1, 2, 3]
# b = [a, 4, 5, 6]
# print(b)
# # [[1, 2, 3], 4, 5, 6]
#
# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)
# # [1, 2, 3, 4, 5, 6]
#
# print(a) # [1, 2, 3]
# print(*a)  # 1 2 3

# def my_func(*args, **kwargs):
#    print(type(args))
#    print(type(kwargs))
#
# my_func()
# # <class 'tuple'>
# # <class 'dict'>

# def adder(*nums):
#    sum_ = 0
#    for n in nums:
#       sum_ += n
#
#    return sum_
#
#
# print(adder())  # 0
# print(adder(1))  # 1
# print(adder(1, 2))  # 3
# print(adder(1, 2, 3))  # 6


# def incorrect_func(name_arg=[]):
#    # name_arg является локальной переменной
#    print("Аргумент до изменения", name_arg)
#    name_arg.append(1)
#    print("Аргумент после изменения", name_arg)
#
# # вызовем два раза одну и ту же функцию
# incorrect_func()
# print('-----')
# incorrect_func()
#
# # Аргумент до изменения []
# # Аргумент после изменения [1]
# # -----
# # Аргумент до изменения [1]
# # Аргумент после изменения [1, 1]


# # установим аргумент name_arg пустым а внутри функции будем проверять его
# def correct_func(name_arg=None):
#    if name_arg is None:
#        name_arg = []
#    print("Аргумент до изменения", name_arg)
#    name_arg.append(1)
#    print("Аргумент после изменения", name_arg)
#
# # вызовем два раза одну и ту же функцию
# correct_func()
# print('-----')
# correct_func()
# print('-----')
# correct_func([123])
# print('-----')
# correct_func(name_arg=[123])
#
# # Аргумент до изменения []
# # Аргумент после изменения [1]
# # -----
# # Аргумент до изменения []
# # Аргумент после изменения [1]
# # -----
# # Аргумент до изменения [123]
# # Аргумент после изменения [123, 1]
# # -----
# # Аргумент до изменения [123]
# # Аргумент после изменения [123, 1]


# def rec_fibb(n):
#    if n == 1:
#        return 1
#    if n == 2:
#       return 1
#    return rec_fibb(n - 1) + rec_fibb(n - 2)
#
# print(rec_fibb(10))  # 55

# # С помощью рекурсивной функции найдите сумму чисел от 1 до n.
# def rec_sum(n):
#    if n == 1:  # терминальный случай
#        return 1
#    return n + rec_sum(n - 1)  # рекурсивный вызов
# print(rec_sum(15))  # 120


# # С помощью рекурсивной функции разверните строку.
# def reverse_str(string):
#    if len(string) == 0:
#        return ''
#    else:
#        return string[-1] + reverse_str(string[:-1])
#
# print(reverse_str('test'))  # tset


# # Дано натуральное число N. Вычислите сумму его цифр.
# def sum_digit(n):
#    if n < 10:
#        return n
#    else:
#        return n % 10 + sum_digit(n // 10)
#
# print(sum_digit(258))  # 15