# Pets polymorphism
# Three classes, all with a different speak method

class Dog():
	def __init__(self, name):
		self.name = name

	def speak(self):
		print(self.name, 'says bark bark.')

class Cat():
	def __init__(self, name):
		self.name = name

	def speak(self):
		print(self.name, 'says meow.')

class Bird():
	def __init__(self, name):
		self.name = name

	def speak(self):
		print(self.name, 'says tweet.')

oDog1 = Dog('Rover')
oDog2 = Dog('Fido')

oCat1 = Cat('Fluffy')
oCat2 = Cat('Max')

oBird = Bird('Jeff')

petsList = [oDog1, oDog2, oCat1, oCat2, oBird]

for Pet in petsList:
	Pet.speak()