//Definition and call of function swap()
//Demonstrates the use of pointers as parameters

#include <iostream>
using namespace std;

void swap(float *, float *); //Prototype of swap()

void swap(float *p1, float *p2)
{
	float temp; //Temporary variable

	temp = *p1; 
	*p1 = *p2;
	*p2 = temp;
}

int main()
{
	float x = 11.1F;
	float y = 22.2F;

	cout << x << endl;
	cout << y << endl;
	swap(&x, &y);
	cout << x << endl;
	cout << y << endl;

	return 0;
}