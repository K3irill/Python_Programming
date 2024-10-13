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

# 
def string_to_number(s):
    return int(s)
# 
def dna_to_rna(dna):
        result = list()
        for molecule in list(dna):
              if molecule == "T":
                    result.append('U')
              else: result.append(molecule)
        return result							
              
print(dna_to_rna("GCAT"))

arr = ['G', 'C', 'A', 'T', 'T', 'G', 'T']

result = [item for item in arr if item == 'T']
# new_arr = ['X' if item == 'T' else item for item in arr] сразу с заменой
print(result)

numbers = [-5, -4, -3 ,-2, -1, 0, 1, 2, 3, 4, 5]
result2 = filter(lambda n: n % 2 == 0 and n != 0, numbers)

for n in result2: print(n, end=' ')

result3 = map(lambda item: 'U' if item == 'T' else item, arr)
newArr = list()
for n in result3: newArr.append(n)
readyStr = ''.join(newArr)
print(readyStr)