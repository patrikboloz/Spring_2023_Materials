
def welcome(name):
	print("Good morning", name, " !")
	summation = name * 2
	print(summation)


#welcome("Patrik")
#welcome("Jeff")
#welcome("Marine")
#welcome(10)

def default_welcome(name = "Human"):
	print("Greetings ", name)

#default_welcome("Bob")
#default_welcome()

def summation(a,b):
	c = a + b
	return c

variable = summation(10, 50)
print(variable * 2)




