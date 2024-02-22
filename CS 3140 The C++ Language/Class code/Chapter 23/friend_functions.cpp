#include <iostream>
using namespace std;

class EquilateralTriangle
{
private:
	float a;
	float circumference;
	float area;
public:
	void setA(float length)
	{
		if (length > 0)
		{
			a = length;
			circumference = a * 3;
			area = (1.73 * a * a) / 4;
		}
	}

	friend void PrintResults(EquilateralTriangle);

	/* You can have multiple friend functions 
	   but choose your friend functions carefully.
	   By having too many friend functions, you
	   break the encapsulation rule.*/
};

void PrintResults(EquilateralTriangle et)
{
	cout << "circumference = "<< et.circumference << endl;
	cout << "area = " << et.area << endl;
}


int main()
{
	EquilateralTriangle et;
	et.setA(3);

	/* Private attributes cannot be accessed!
	cout << "circumference = "<< et.circumference << endl;
	cout << "area = " << et.area << endl;
	*/

	PrintResults(et);

	return 0;	
}