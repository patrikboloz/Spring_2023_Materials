# Definition of a factorial function implemented in Python
# This example is using recursion


def factorial(n):
	if n == 0: #base case
		return 1 
	else: #recursive case
		return n * factorial(n - 1) #recursion = calling the function inside of the same function


print(factorial(5))
print(factorial(0))