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

void operator<<(ostream& COUT, BankAccount& bnkAccount)
{
	COUT << "Name " << bnkAccount.Name << endl;
	COUT << "Balance " << bnkAccount.Balance << endl;
}

int main()
{
	BankAccount bankacc1 = BankAccount("Patrik", 82000);
	cout << bankacc1;

	return 0;
}