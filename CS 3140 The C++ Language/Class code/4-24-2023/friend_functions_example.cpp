#include <iostream>
using namespace std;

class EquilateralTriangle
{
private:
	float a, circumference, area;
public:

	void setA(float length)
	{
		if (length > 0)
		{
			a = length;
			circumference = a * 3;
			area = (1.73 * a * a)/4;
		}
	}

	friend void PrintResults(EquilateralTriangle);

};

void PrintResults(EquilateralTriangle ET)
{
	cout << "circumference = " << ET.circumference << endl;
	cout << "area = " << ET.area << endl;
}

int main()
{
	EquilateralTriangle et;
	et.setA(20);

	//cout << "circumference" << et.circumference << endl;
	//cout << "area = " << et.area << endl;

	PrintResults(et);

	return 0;
}