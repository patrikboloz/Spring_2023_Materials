class Person():

	def __init__(self, name, salary):
		self.__name = name
		self.__salary = salary


	def _retirement(self):
		self.__salary = self.__salary - 500
		return self.__salary 

	def getSalary(self): #returning the protected __salary variable
		return self.__salary

	def setSalary(self, update):
		self.__salary = update
		return self.__salary



oPerson1 = Person("Patrik", 20000)

print(oPerson1._retirement())
print(oPerson1.getSalary())
print(oPerson1.setSalary(40000))
