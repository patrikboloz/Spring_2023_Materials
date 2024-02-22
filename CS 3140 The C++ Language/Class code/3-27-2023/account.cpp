//Defines methods init() and display()

#include "account.h"
#include <iostream>
#include <iomanip>
using namespace std;

// The method init() copies the given arguments into the private members of the class

bool Account::init(const string& i_name,
	               unsigned long i_nr,
	               double        i_balance)

{
	if (i_name.size() < 1)
		return false;

	name = i_name;
	nr = i_nr;
	balance = i_balance;
	return true;
}

//The method display() outputs private data
void Account::display()
{
	cout << fixed << setprecision(2)
	     << "--------------------------------------" << '\n'
	     << "Account holder:   " << name << '\n'
	     << "Account number:   " << nr << '\n'
	     << "Account balance:  " << balance << '\n'
	     << "--------------------------------------"
	     << endl;
}

Account::Account( const string& a_name, unsigned long a_nr, double a_state)
{
	nr = a_nr;
	name = a_name;
	balance = a_state;
}

Account::Account(const string& a_name)
{
	name = a_name;
	nr = 11111111;
	balance = 0.0;
}