def binary_search(at, user, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if at[middle] == user:
            return middle - 1
        elif user < at[middle]:
            return binary_search(at, user, left, middle - 1)
        else:
            return binary_search(at, user, middle + 1, right)
    except IndexError:
        return 'Число выходит за диапазон списка, введите меньшее число.'

spisok = '67 14 3 81 93 2 79 22 18 57 26 30 '
at = [int(x) for x in spisok.split()]
print("Список до сортировки: ", at)

try:
    user = int(input("Введите целое двухзначное число : "))
    if user < 100 and user > -100:
        at.append(user)
        #print("Список до сортировки: ", at)
        at.sort()
        #print("Список после сортировки по возрастанию: ", at)
    else:
        print("введите корректное число")
except ValueError:
    print("Не корректные данные.")
    print("Программа завершена!")
a = binary_search(at, user, 0, len(at)-1)
print("Индекс числа, которое меньше введенного пользователем числа: ", a)
del at[a+1]
print("Список после сортировки по возрастанию: ", at)

