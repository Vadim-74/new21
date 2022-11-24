# myfile = open('hell.txt', 'r')
# file = myfile.read()
# print(file)
# myfile.close()
import json

# # Исключения
# try:
#     somefile = open('hello1.txt', 'w')
#     try:
#         somefile.write('hello world')
#     except Exception as e:
#         print(e)
#     finally:
#         somefile.close()
# except Exception as ex:
#     print(ex)


# with open('hello2.txt', 'w') as somefile:
#     somefile.write('goodbye world!')

# with open('17-4.txt', 'a') as file:
#     file.write('\nbye world')


# with open('17-4.txt') as f:
#     a = f.readlines()
#     b = [int(x) for x in a]
#     # b = list(map(int, a))  # ==  b = [int(x) for x in a]
#     print(a)
#     print(b)
#     print(b[2])


# with open('17-4.txt') as f:
#     s = f.readlines()
#     a = list(map(int, s))
#     res = []
#     for i in a:
#         if str(i).count('0') >= 2 and i % 7 == 0: # больше двух нулей и делится на 7
#             res.append(i)
# print(max(res), len(res))  # максимальное число и количество чисел


# #  Находим является ли последняя цифра числа 7-й и число делится на 12
# with open('17-4.txt') as f:
#     s = [int(x) for x in f]
#     res = []
#     for i in range(1, len(s)):
#         if (abs(s[i]) % 10 == 7 or abs(s[i-1]) % 10 == 7) and (s[i]+s[i-1]) % 12 == 0:
#             res.append(s[i]+s[i-1])
# print(len(res), max(res))


# #  Максимальное количество идущих подряд символов,
# #  среди которых каждые два соседних различны
# with open('17-4.txt') as f:
#     s = f.readline()
#     m = 1
#     k = 1
#     for i in range(1, len(s)):
#         if s[i] != s[i-1]:
#             k += 1
#             m = max(k, m)
#         else:
#             k = 1
# print(m)

# # Подсчитать количество слов
# with open('17-4.txt') as f:
#     s = f.read()
#     m = s.split()
#     print(len(m))


# # JSON
# import json
# data = {
#     "name": "Ivan",
#     "age": 26,
#     "city": "Saratov"
# }

# with open('data_file.json', 'w') as f:
#     json.dump(data, f)

with open('data_file.json', 'r') as f:
    data = json.load(f)
    print(data)






