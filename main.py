 
from random import randint
# import this
# import antigravity
print('js top)')

# phrase = input('enter phrase')

name = 'user'

print(f"Good morning, {name}")

print(f"{777:0>9}")
print(f"{777:0<9}")
print(f"{777:0^9}")

print("-" * 10)

str1 = '12'
num = 12
print(type(int(str1)))
print(type(str(num)))

width = '825.5'
height = '500.5'
s = float(width) + float(height)
print(s)

floatNum = 12.991
floatNumRounded = f"{floatNum:.1f}"
print(floatNumRounded)
print((width + '\n') * 3)

print(10 // 2)
print(10 / 2)

print(10 > 100 or 5 > 100 or 10 > 0)
print(10 > 100 and 5 > 100 and 10 > 0)
print(not False)
print(not 2 > 0)

if 2 > 2 and 2 < 4: 
	print('yes, its true')
elif 10 * num > 2:
	print('big')
else:
	print('no, its false')

x = randint(1, 100)
print(x)

for i in range(5):
	print(i)

for letter in 'EVERYONE':
	print(letter)

for x in range(10, 20, 3): 
    print(x)

total_num = 0
for x in range(1, 5 + 1): 
    total_num += x

print(total_num)

while total_num < 25:
	if total_num == 20:
		print('already ' + str(total_num))
	print(total_num)
	total_num += 1
else: 
	print('end')

