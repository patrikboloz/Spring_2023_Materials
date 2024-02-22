
class Animal():

	def __init__(self, animal_name):
		self.name = animal_name

	def speak(self):
		print(self.name, "is speaking!")

	def sleep(self, sleep_time):
		print(self.name, "is sleeping for", sleep_time, "hours.")

	def change_name(self, new_name):
		self.name = new_name
		return self.name

animal1 = Animal("Frosty")
#print(animal1.name)

animal2 = Animal("Sofia")
#print(animal2.name)

animal1.speak()
animal2.speak()

animal1.sleep(8)
animal2.sleep(5)

new_name = animal1.change_name("Fred")
print(new_name)




