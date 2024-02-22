//Example for a siumple function returning a value

#include <iostream>
#include <iomanip>
using namespace std;

double area(double, double); //Prototype

double area(double width, double len)
{
	//Computes the area of a rectangle.
	return (width * len); //Returns the result
}

int main()
{
	double x = 3.5, y = 7.2, res;

	res = area(x, y+1); //Call

	//To output to two decimal spaces:
	cout << fixed << setprecision(2);
	cout << "\n The area of a rectangle"
	     << "\n with width " << setw(5) << x
	     << "\n and lenght " << setw(5) << y+1
	     << "\n is         " << setw(5) << res
	     << endl;
	return 0;
}