number = int(input("Choose a number between 0 - 50: "))
factorial = 1
if number < 0:
	print("Cannot perform the calculation, the number you entered was negative!")
elif number > 50:
	print("Cannot perform the calculation, the number you entered was bigger than 50!")
else:
	for i in range(1, number + 1):
		factorial = factorial * i
	print("The factorial of", number, "is:", factorial)
