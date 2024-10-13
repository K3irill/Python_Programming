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