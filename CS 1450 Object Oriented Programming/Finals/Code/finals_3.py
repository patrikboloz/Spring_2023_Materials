import random

def greetings(name):
	print("Hello ", name)
	weather = ["Rainy", "Sunny", "Cloudy", "Cold"]
	print("Today's weather is:", random.choice(weather))

greetings("Patrik")


