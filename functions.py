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