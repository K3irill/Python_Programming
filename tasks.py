product = 'черешня'
cost = 2
weight = 3
money = 10

total = weight * cost
change = f"{money - total:.0f}"

print('Чек' + '\n' + str(product) + ' - ' + str(weight) +  ' - ' + str(cost) + 'руб/кг' + '\n' + 'Итого: ' + str(total) + 'руб' + '\n' + 'Внесено: ' + str(money) + 'руб' + '\n' + 'Сдача: ' + str(change) + 'руб')


cost = 38
weightProduct = 2.5
money = 100
print(f"{money - (cost * weightProduct):.0f}")

print(f"{money - (2.5 * 38):.0f}")