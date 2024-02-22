//Using arrays of char and pointers to char

#include <iostream>
using namespace std;

int main()
{
	cout << "Demonstrating arrays of char and pointers to char." << endl;

	char text[] = "Good morning!", name[] = "Bill!";
	char *cPtr = "Hello ";

	cout << cPtr << name << "\n" 
	     << text << endl;

	cout << "The text \"" << text
	     << "\" starts at address " << (void*)text << endl;

	cout << text + 4 << endl;

	cPtr = name;

	cout << "This is the " << *cPtr << " of " << cPtr << endl;

	*cPtr++;
	*cPtr = 'k';
	cout << cPtr << endl;


	float v[6] = {0.0, 0.1, 0.2, 0.3, 0.4, 0.5}, *pv, x;

	pv = v + 4;
	cout << *pv << endl;
	*pv = 1.4;
	cout << *pv << endl;

	return 0;

}