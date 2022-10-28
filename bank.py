money = input("Введите сумму вклада:")

per_cent = {'ТКБ': float(money) / 100 * 5.6, 'СКБ': float(money) / 100 * 5.9, 'ВТБ': float(money) / 100 * 4.28,
            'СБЕР': float(money) / 100 * 4.0}

print("Максимальная сумма, которую вы можете заработать", max(per_cent.values()), "руб.")
print(money)
