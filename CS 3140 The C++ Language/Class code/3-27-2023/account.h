//Defining the class Account
//Updated definition of class Account with inline methods

#ifndef _ACCOUNT_ //Avoid multiple inclusions
#define _ACCOUNT_ 

#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

class Account
{
private: //Sheltered members
	string name; //Account holder
	unsigned long nr; //Account number
	double balance; //Account balance

public: //Public interface
	Account(const string& a_name = "X", 
		    unsigned long a_nr = 11111111L, 
		    double a_state = 0.0)
	{
		name = a_name; nr = a_nr; balance = a_state;
	}
	~Account(){} //Dummy desctructor: implicit inline

	//Access methods:
	const string& getName(){ return name;}
	bool setName(const string& s)
	{
		if (s.size() < 1) //No empty name
			return false;
		name = s;
		return true;
	}

	unsigned long getNr() {return nr;}
	void setNr(unsigned long n) {nr = n;}
	double getState(){return balance;}
	void setState(double x) {balance = x;}

	void display();
};

inline void Account::display() //Explicit inline
{
	cout << fixed << setprecision(2)
	     << "--------------------------------------" << '\n'
	     << "Account holder:   " << name << '\n'
	     << "Account number:   " << nr << '\n'
	     << "Account balance:  " << balance << '\n'
	     << "--------------------------------------"
	     << endl;
}


#endif // _ACCOUNT_