values = [1,2,3,4,5,6]
print(values[0])
print(values[-1])
for num in values:
	print(num)

letters = list('abcdef')
print(letters)

even_numbers = list(range(0, 20, 2))
print(even_numbers)

# len
print(len(even_numbers))
print(len('typescript'))

# splice

fruits = ['Apple', 'Grape', 'Peach', 'Banan', 'Orange']
part_of_fruits = fruits[0:3]
print(part_of_fruits)

# print(fruits[0:2])
print(fruits[:2])
# print(fruits[0:len(fruits)])
print(fruits[::])

print(fruits[::2])
print(fruits[::-1])

for fruit in fruits:
    print(fruit, end=' ')

for index in range(len(fruits)):
  	print(fruits[index], end=' ')

if 'Apple' in fruits:
  	print('В списке есть элемент Apple')

fruits.append('mango')
fruits.insert(0, 'тут будет вишня')
fruits.pop(0)#получается не будет вишни

# Чтобы удалить последний элемент, вызвать метод pop без аргументов
fruits.pop()

#удалить элемент зная название

fruits.remove('Orange')


#
fruits.append('Apple')
fruits.append('Apple')
fruits.insert(0, 'Apple')
# посчитать сколько одинаковых элементов в списке
print(fruits.count('Apple'))

#  сортировка 
numbers = [100, 2, 11, 9, 3, 1024, 567, 78]
numbers.sort()
print(numbers)


print(numbers[::-1])
numbers.reverse()
print(numbers)

fruits.extend(numbers)
print(fruits)

fruits.clear()# почистим список

fruits = ['Banana', 'Apple', 'Grape']
print(fruits.index('Apple'))# узнать индекс по названию

new_fruits = fruits.copy()