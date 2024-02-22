#include <iostream>
#include "result.h"
using namespace std;

int main()
{
	//Result temperature1(18.5);
	//Result temperature2(15.4, 14, 15, 35);
	
	DayTime morning(6, 30);
	Result t1, //default constructor
	       t2(12.5, morning),
	       t3(18.2, 12, 0, 0),
	       t4(17.7); //at current time

	cout << "Default values: ";
	t1.print();
	cout << "\n Temperature   Time   \n"
	     << "--------------------------" << endl;
	t2.print();
	t3.print();
	t4.print();
	cout << endl;
	return 0;


} 