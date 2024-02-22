#Lab 3
"""Your task will be to create a game of higher or lower. By creating a higher_or_lower function, the user will
play against the computer, where the computer will randomly choose between numbers 0 and 100 and the user
will have 5 tries to guess the number. The computer will say higher, if the user's number is lower than the
computer's, and computer will say lower, if the user's number is higher than the compputers one. The game ends
if the user chooses/guesses the right number or if they don't answer in 5 tries. 
Use the random library to randomize the computer's number between 0 and 100
Use the input() function to get the input from the user. (Don't forget that you need to convert an input from
a string to a number)
Use if statements to compare the results
Use a while loop to see how many tries the user has. 

EXTRA CREDIT: Create a class out of this game, import it in another file called game.py and initialize the game
in the game.py file.""" 


class higherOrLower():

	def __init__(self, N, tries):

		self.N = N
		self.tries = tries

	def play(self):


		count = 0
		print("This is a game of higher or lower.\n")
		computer_random = random.randrange(0, 100)
		while count <= self.tries:
		
			users_number = int(input("Please write a number, that you'll want to guess."))

			if users_number == computer_random:
				print("You've won the game! The computer's number was", computer_random)
				break
			elif users_number > computer_random:
				print("Lower")
			elif users_number < computer_random:
				print("Higher")

		count = count + 1

		if count > 5:
			print("The computer's number was", computer_random)
			print("You've run out of your tries. The computer wins!")














import random

def higher_or_lower():

	count = 0
	print("This is a game of higher or lower.\n")
	computer_random = random.randrange(0, 100)
	while count <= 5:
		
		users_number = int(input("Please write a number, that you'll want to guess."))

		if users_number == computer_random:
			print("You've won the game! The computer's number was", computer_random)
			break
		elif users_number > computer_random:
			print("Lower")
		elif users_number < computer_random:
			print("Higher")

		count = count + 1
	if count > 5:
		print("The computer's number was", computer_random)
		print("You've run out of your tries. The computer wins!")

higher_or_lower()