def isEven(num = 10):
	if num % 2 == 0:
		return True
	else:
		return False
	
print(isEven(8))
print(isEven(7))

users = [
    { 'name': "alex", 'age': 12 },
    { 'name': "mike", 'age': 24 },
    { 'name': "masha", 'age': 16 },
    { 'name': "stas", 'age': 18 },
];

def sortStudents(arr):
	result = []
	for user in arr:
		if user['age']  > 18:
			result.append(user['name'])
	return result

print(sortStudents(users))

x = 2
def func():
	global x 
	x = 3

	return print(x)

func()
print(x)

def total(a=5, *numbers, **phonebook):
    print('a', a)

    for single_item in numbers:
        print('single_item', single_item)

    for first_part, second_part in phonebook.items():
        print(first_part,second_part)

print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))


message = lambda: print('let\'s go ')
message()