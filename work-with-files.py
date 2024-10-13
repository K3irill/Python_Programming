file = open('for-test.txt', 'w')
file.write('JAVASCRIPT\n')
file.write('PYTHON\n')
file.write('TYPESCRIPT\n')
file.close()

try:
	with open('tasks.py', encoding='utf-8') as f:
		text = f.read()
		print(text)
except FileNotFoundError:
	print("Файл не найден. Убедитесь, что файл tasks.py существует.")
except UnicodeDecodeError:
    print("Ошибка декодирования. Убедитесь, что файл закодирован в UTF-8.")