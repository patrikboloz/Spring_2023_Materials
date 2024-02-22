//Uses objects of class Account

#include "account.h"
#include "account.cpp"

int main()
{
	Account current1, current2;

	current1.init("Cheers, Mary", 12345,-1200);
	current1.display();

	//current1.balance += 100;

	current2.init("Jones, Tom", 4514441, 1500);
	current2.display();

	Account& mtr = current1;
	mtr.display();

	return 0;
}