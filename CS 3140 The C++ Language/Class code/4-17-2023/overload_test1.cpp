#include <iostream>
#include <string>
using namespace std;

struct BankAccount
{
	string Name;
	int Balance;

	BankAccount(string name, int balance)
	{
		Name = name;
		Balance = balance;
	}
};

ostream& operator<<(ostream& COUT, BankAccount& bnkAccount)
{
	COUT << "Name: " << bnkAccount.Name << endl;
	COUT << "Balance: " << bnkAccount.Balance << endl;
	return COUT;
}

int main()
{
	BankAccount bankacc1 = BankAccount("Patrik", 80000);
	BankAccount bankacc2 = BankAccount("Jeff", 45000);
	cout << bankacc1;
	cout << bankacc2;
	cout << bankacc1 << bankacc2;
	//operator<<(cout, bankacc1); this is the same as cout << bankacc1;


	return 0;
}