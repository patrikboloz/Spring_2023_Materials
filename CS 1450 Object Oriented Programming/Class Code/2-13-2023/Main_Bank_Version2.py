#Test program using accounts
#Version 2, using a list of accounts

#Bring all the code from the Account class file
from Account import *

#Start off with an empty list of accounts
accountsList = []

#Create two accounts
oAccount = Account('Joe', 100, 'JoesPassword')
accountsList.append(oAccount)
print("Joes account number is 0")

oAccount = Account('Mary', 12345, 'MarysPassword')
accountsList.append(oAccount)
print("Marys account number is 1")

#rint(accountsList)

accountsList[0].show()
accountsList[1].show()

#Call some methods on these two objects
print('Calling methods of the two accounts...')
accountsList[0].deposit(50, 'JoesPassword')
accountsList[1].withdraw(345, 'MarysPassword')

#Show the accounts
accountsList[0].show()
accountsList[1].show()


#Create another account with infromation from the user
print()
userName = input('What is the name of this account?')
userBalance = input('What is the starting balance?')
userPassword = input('What is the users password?')

userBalance = int(userBalance) #typecasting 

oAccount = Account(userName, userBalance, userPassword)
accountsList.append(oAccount)

#Show the newly created account
print('Created a new account, account number is 2')
accountsList[2].show()

#Lets deposit 100 into the new account
accountsList[2].deposit(100, userPassword)
usersBalance = accountsList[2].getBalance(userPassword)
print("After depositing 100 into the account, the balance is", usersBalance)

accountsList[2].show()