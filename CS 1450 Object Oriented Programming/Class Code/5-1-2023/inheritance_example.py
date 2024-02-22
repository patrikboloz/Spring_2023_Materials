#Inheritance

class Animal():

	def __init__(self, animal_name, animal_type = "Generic"):
		self.animal_type = animal_type
		self.name = animal_name 

	def speak(self):
		print(self.name, "is speaking!")

	def sleep(self, sleep_time):
		print(self.name, "is sleeping for", sleep_time, "hours.")

	def set_Name(self, new_name):
		self.name = new_name
		return self.name

	def get_Name(self): 
		return self.name


class Bird(Animal):

	def speak(self):
		print(self.name, "is tweeting!")

class Dog(Animal):
	
	def speak(self): #polymorphism = changing the hidden implementation while keeping the method name
		print(self.name, "is barking!") 


bird1 = Bird("Frosty")
print(bird1.get_Name())

bird2 = Bird("Sofia")
print(bird2.get_Name())

dog1 = Dog("Lassie")
print(dog1.get_Name())

dog1.speak()
bird1.speak()


