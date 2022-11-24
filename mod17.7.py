# вернуть индекс первого вхождения
# элемента, если он входит в него, и False если не входит.
def find(array, element):
    for i, a in enumerate(array):
        if a == element:
            return i
    return False

array = list(map(int, input().split()))
element = int(input())

print(find(array, element))


# функцию count, которая возвращает количество вхождений элемента в массив
def count(array, element):
    count = 0
    for a in array:
        if a == element:
            count += 1
    return count

