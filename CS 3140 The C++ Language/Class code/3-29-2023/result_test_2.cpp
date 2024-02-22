//Test the second version of the Result class

#include "result2.h"
#include <iostream>
using namespace std;

int main()
{
	DayTime start(10,15);
	Result m1(101.1, start), 
	       m2(m1),
	       m3(99.9); //Current time
}