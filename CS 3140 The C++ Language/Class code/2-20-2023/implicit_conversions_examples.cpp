#include <iostream>
using namespace std;

int main()
{
	//Example 1
	int i = 100;
	long lg = i + 50; //Result of type int is converted to long

	//Example 2
	long lg = 0x654321; short st;
	st = lg //0x4321 is assigned to st.

	//Example 3
	int i = -2; unsigned int ui = 2;
	i = i * ui 
	//First the value contained in i is convereted to unsigned int
	//(preserving the bit pattern) and multiplied by 2 (overflow!).
	//While assigning the bit pattern the result is interpreted as
	//an int value again, i.e. -4 is stored in i

	//Example 4
	double db = -4.567;
	int i; unsigned int ui;
	i = db; //Assigning -4 
	i = db - 0.5 //Assigning -5
	ui = db; //-4 is incompatible with ui

	//Example 5
	double d = 1.23456789012345;
	float f;
	f = d; //1.234568


}