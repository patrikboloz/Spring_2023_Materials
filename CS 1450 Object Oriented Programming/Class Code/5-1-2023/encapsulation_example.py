#Use of setters and getters is needed, since direct access is prohibited
#whenever the notion of encapsulation is to be used.

class Animal():

	def __init__(self, animal_name):
		self.__name = animal_name #privatizing the value self.__name

	def speak(self):
		print(self.__name, "is speaking!")

	def sleep(self, sleep_time):
		print(self.__name, "is sleeping for", sleep_time, "hours.")

	def set_Name(self, new_name): #setter
		self.__name = new_name
		return self.__name

	def get_Name(self): #getter
		return self.__name

animal1 = Animal("Frosty")
print(animal1.get_Name())

animal2 = Animal("Sofia")
print(animal2.get_Name())

print(animal1.set_Name("Bob"))