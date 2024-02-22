# Account class

class Account():

	def __init__(self, name, balance, password):
		self.name = name
		self.balance = balance
		self.password = password

	def deposit(self, amountToDeposit, password):
		if password != self.password:
			print('Sorry, that is the incorrect password!')
			return None

		if amountToDeposit < 0:
			print('You cannot deposit a negative amount!')
			return None

		self.balance = self.balance + amountToDeposit
		return self.balance

	def withdraw(self, amountToWithdraw, password):
		if password != self.password:
			print('Sorry, that is the incorrect password!')
			return None

		if amountToWithdraw < 0:
			print('You cannot deposit a negative amount!')
			return None

		if amountToWithdraw > self.balance:
			print('You cannot withdraw more than you have in your account!')
			return None

		self.balance = self.balance - amountToWithdraw
		return self.balance

	def getBalance(self, password):
		if password != self.password:
			print('Sorry, incorrect password')
			return None
		return self.balance

	#Added for debugging
	def show(self):
		print(' Name:', self.name)
		print(' Balance:', self.balance)
		print(' Password:', self.password)
		print()

#test_account = Account('Test', 900, 'password')
#test_account.show()
#test_account.deposit(100, 'password')
#print(test_account.getBalance('password'))

#test_account.withdraw(550, 'password')
#print(test_account.getBalance('password'))