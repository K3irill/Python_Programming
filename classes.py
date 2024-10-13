class Vehicle:
	def __init__(self, title, type):
		self.__title = title
		self.__type = type

	def display_info(self):
		print(f"Name: {self.__title} Type: {self.__type}")
	

	def get_title(self):
		return self.__title
	# or------------------|
	@property
	def title(self):
		return self.__title
	# --------------------|
	def get_type(self):
		return self.__type
	# or------------------|
	@property
	def type(self):
		return self.__type
	# --------------------|
	def set_type(self, type):
		self.__type = type
	# or -----------------|
	@type.setter
	def type(self, type):
		self.__type = type
	# --------------------|

	def __del__(self):
		print(f'Vehicle {self.__title} was deleted')


plane = Vehicle('S-777', 'plane')
plane.display_info()

plane.set_type('helicopter')
plane.display_info()


class Engine(Vehicle):

	def __init__(self, title, type, horsepower):
		super().__init__(title, type)
		self.__horsepower = horsepower

	def display_info(self):
		super().display_info()
		print(f'Engine of {self.title} has {self.__horsepower} horsepower')

	def start(self):
		print(f'Engine of {self.title} is starting...')
	
 

engineMoto = Engine('Kawasaki', 'Motorcycle', 310)

engineMoto.start()
engineMoto.display_info()


class Person:
 
    def __init__(self, name):
        self.__name = name   # имя человека
 
    @property
    def name(self):
        return self.__name
 
    def display_info(self):
        print(f"Name: {self.__name}")
 
 
class Employee(Person):
 
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company
 
    def display_info(self):
        super().display_info()
        print(f"Company: {self.company}")
 
    def work(self):
        print(f"{self.name} works")