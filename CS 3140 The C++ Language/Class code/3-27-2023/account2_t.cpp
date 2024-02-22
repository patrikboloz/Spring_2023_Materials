//Using the constructors of class Account

#include "account.h"
#include "account.cpp"

int main()
{
	Account giro("Cheers, Mary", 12345678, -1200), save("Lucky, Luke");
	//Account depo;
	giro.display();
	save.display();

	Account temp("Funny, Alex", 77777777, 500);
	save = temp;

	save.display();
	save.init("Lucky, Patrick", 46847182, 1000);
	save.display();
	temp.display();

	return 0;




}