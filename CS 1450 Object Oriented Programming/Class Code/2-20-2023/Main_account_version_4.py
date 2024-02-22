#Interactive test program creating a dictionary of accounts
#Version 4. with an interactive menu

from Account import *

accountsDict = {}
nextAccountNumber = 0

#Create two accounts:
oAccount = Account('Joe', 100, 'JoesPassword')
joesAccountNumber = nextAccountNumber
accountsDict[joesAccountNumber] = oAccount
print("Account number for Joe is:", joesAccountNumber)
nextAccountNumber = nextAccountNumber + 1

oAccount = Account('Mary', 13245, 'MarysPassword')
marysAccountNumber = nextAccountNumber
accountsDict[marysAccountNumber] = oAccount
print("Account number for Mary is:", marysAccountNumber)
nextAccountNumber = nextAccountNumber + 1

#show the information
accountsDict[joesAccountNumber].show()
accountsDict[marysAccountNumber].show()

#Create an interactive menu

while True:
	print()
	print("Welcome to the Bank of Las Vegas, please choose from these options:")
	print("Press b to get the balance")
	print("Press d to make a deposit")
	print("Press w to make a withdrawal")
	print("Press o to open a new account")
	print("Press s to show all accounts")
	print("Press q to quit")
	print()

	action = input("What do you want to do?")
	print()

	if action == 'b':
		print("Getting the balance")
		userAccountNumber = input("Please enter the account number: ")
		userAccountNumber = int(userAccountNumber)
		userAccountPassword = input("Please enter the password: ")
		oAccount = accountsDict[userAccountNumber] 
		theBalance = oAccount.getBalance(userAccountPassword)
		if theBalance is not None:
			print("Your balance is: ", theBalance)

	elif action == 'd':
		print("Depositing into an account")
		userAccountNumber = input("Please enter the account number: ")
		userAccountNumber = int(userAccountNumber)
		userAccountPassword = input("Please enter the password: ")
		userDepositAmount = input("Please enter amount to deposit: ")
		userDepositAmount = int(userDepositAmount)
		oAccount = accountsDict[userAccountNumber]
		theBalance = oAccount.deposit(userDepositAmount, userAccountPassword)
		if theBalance is not None:
			print("Your balance is: ", theBalance)

	elif action == 'o':
		print("Opening a new account")
		userName = input("What is the name for the new user account? ")
		userStartingAmount = input("What is the starting balance for this account? ")
		userStartingAmount = int(userStartingAmount)
		userPassword = input("What is the password for this new account? ")
		oAccount = Account(userName, userStartingAmount, userPassword)
		accountsDict[nextAccountNumber] = oAccount
		print("Your new account number is:", nextAccountNumber)
		nextAccountNumber = nextAccountNumber + 1
		print()

	elif action == 's':
		print("Showing all the accounts:")
		for userAccountNumber in accountsDict:
			oAccount = accountsDict[userAccountNumber]
			print('Account number:', userAccountNumber)
			oAccount.show()

	elif action == 'q':
		break

	elif action == 'w':
		print("Withdrawing some money")
		userAccountNumber = input("Please enter your account number: ")
		userAccountNumber = int(userAccountNumber)
		userWithdrawalAmount = input("Please enter the amount to withdraw: ")
		userWithdrawalAmount = int(userWithdrawalAmount)
		userPassword = input("Please enter the password: ")
		oAccount = accountsDict[userAccountNumber]
		theBalance = oAccount.withdraw(userWithdrawalAmount, userPassword)
		if theBalance is not None:
			print("Withdrew:", userWithdrawalAmount)
			print("Your new balance is:", theBalance)

	else:
		print("Sorry, that was not a valid action. Try again!")