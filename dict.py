developer = dict(name='Kail', age='20', for_del= True)

del developer['for_del']
print(developer)

developerAn = {
	'name': 'Kail',
	'age': 20,
	"city": 'Moscow',
}

print(developerAn.get('age'))
print(developerAn.get('street', 'No age'))

sneakers = dict(brand='Adidas', price='9990 RUB', model='Nite Jogger')

model = sneakers.pop('model')

print(sneakers.keys())

keysOfDict = list(sneakers.keys())
print(keysOfDict)

print(sneakers.values())
values = list(sneakers.values())

print(sneakers.items())

items = list(sneakers.items())

for key in sneakers:
	print(key)

for value in sneakers.values():
	print(value)

student = dict(name='Ivan', age=12)
student.setdefault('lastname', 'Kabanov')
print(student)

# кортеж

T = (1,2,3,4)
len(T)
T = T + (5,6)
print(T)

# сеты(уникумы)

cities = ['Санкт-Петербург', 'Хабаровск', 'Казань', 'Санкт-Петербург', 'Казань']
un_cities = set(cities)

un_cities.add('Волгоград')

un_cities.discard('Волгоград')

un_cities.clear()
print(un_cities)

# Проверяет, состоит ли строка из одних только цифр
"a".isdigit() #False
"a10".isdigit() #False
"10".isdigit() #True
# isalpha()

# Проверяет, состоит ли строка из одних букв:

"a".isalpha() #True
"a100".isalpha() #False
"a--  ".isalpha() #False
"a ".isalpha() #False
# isalnum()

# позволяет проверить, состоит ли строка из букв или цифр:

"a".isalnum() #True
"a10".isalnum() #True