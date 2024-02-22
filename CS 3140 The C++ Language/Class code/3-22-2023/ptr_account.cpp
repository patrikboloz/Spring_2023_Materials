//Uses pointers to objects of class Account
#include "account.h"
#include "account.cpp" //includes <iostream, <string>

bool getAccount(Account *pAccount); //Prototype

bool getAccount(Account *pAccount)
{
	string name, line(50, '-'); //Local variables
	unsigned long nr;
	double startcapital;

	cout << line << '\n'
		 << "Enter data for a new account: \n"
		 << "Account holder: ";

	if (!getline(cin, name) || name.size() == 0)
		return false;
	cout << "Account number:  ";
	if (!(cin >> nr))  return false;
	cout << "Starting capital:  ";
	if ( !(cin >> startcapital))  return false;

	//All input ok
	pAccount->init(name, nr, startcapital);
	return true;
}

int main()
{
	Account current1, current2, *ptr = &current1;

	ptr->init("Cheer, Mary", 1854158485, 99); //current1.init(.....)
	ptr->display(); //current1.display()

	ptr = &current2; //Let ptr point to current2
	if (getAccount(ptr))
		ptr->display();
	else
		cout << "Invalid input!" << endl;
	return 0;
}