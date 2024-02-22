#Test program using accounts
#Version 3, using a dictionary of accounts

#Bring in all the code from Account class file
from Account import *

accountsDict = {}
nextAccountNumber = 0

# Create two accounts
oAccount = Account('Joe', 100, 'JoesPassword')
joesAccountNumber = nextAccountNumber
accountsDict[joesAccountNumber] = oAccount
print("Account number for Joe is:", joesAccountNumber)
nextAccountNumber = nextAccountNumber + 1

oAccount = Account('Mary', 12345, 'MarysPassword')
marysAccountNumber = nextAccountNumber
accountsDict[marysAccountNumber] = oAccount
print("Account number for Mary is:", marysAccountNumber)
nextAccountNumber = nextAccountNumber + 1

accountsDict[joesAccountNumber].show()
accountsDict[marysAccountNumber].show()
print()

#Call some methods on the different accounts
print("Calling some methods...")
accountsDict[joesAccountNumber].deposit(50, 'JoesPassword')
accountsDict[marysAccountNumber].withdraw(345, 'MarysPassword')
accountsDict[marysAccountNumber].deposit(100, 'MarysPassword')

#Show the modified objects
accountsDict[joesAccountNumber].show()
accountsDict[marysAccountNumber].show()


#Create another account with information from the user
print()
userName = input("What is the name for the new user account?")
userBalance = input("What is the starting balance for this account?")
userPassword = input("What is the password for this account?")
userBalance = int(userBalance) #type casting/type conversion

oAccount = Account(userName, userBalance, userPassword)
newAccountNumber = nextAccountNumber
accountsDict[newAccountNumber] = oAccount
print("Account number for new user account is:", newAccountNumber)
nextAccountNumber = nextAccountNumber + 1

#Show the newly created user account
accountsDict[newAccountNumber].show()

#Let's deposit some money into the new user account
accountsDict[newAccountNumber].deposit(100, userPassword)
userBalance = accountsDict[newAccountNumber].getBalance(userPassword)
print()
print("After depositing 100 into the new account, the user's balance is:", userBalance)
accountsDict[newAccountNumber].show()
