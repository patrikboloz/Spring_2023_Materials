// Demonstrates the use of return values with reference type


#include <iostream>
#include <string>
using namespace std;

double& refMin (double&, double&); //Returns a reference to the minimum

double& refMin(double& a, double& b)
{
	return a <= b ? a : b;
}

int main()
{
	double x1 = 1.1, x2 = x1 + 0.5, y;

	y = refMin(x1, x2); //Assigns the minimum to y.
	cout << "x1 = " << x1 << "   "
	     << "x2 = " << x2 << endl;
	cout << "Minimum: " << y << endl;


	++refMin(x1, x2); //++x1 , as x1 is minimal
	cout << "x1 = " << x1 << "   " //x1 = 2.1
	     << "x2 = " << x2 << endl; //x2 = 1.6

	++refMin(x1, x2); //++x2 , as x2 is minimal
	cout << "x1 = " << x1 << "   " //x1 = 2.1
	     << "x2 = " << x2 << endl; //x2 = 2.6

	refMin(x1,x2) = 10.1; //x1 became 10.1, because x1 was smaller than x2
	cout << "x1 = " << x1 << "   "
	     << "x2 = " << x2 << endl;

	refMin(x1, x2) += 5.0; 
	cout << "x1 = " << x1 << "   "
	     << "x2 = " << x2 << endl;


	return 0;
}