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

	//friend void PrintResults(EquilateralTriangle);

	/* You can have multiple friend functions 
	   but choose your friend functions carefully.
	   By having too many friend functions, you
	   break the encapsulation rule.*/

	friend class Homework;
};

class Homework
{
public:
	void PrintResults(EquilateralTriangle et)
{
	cout << "circumference = "<< et.circumference << endl;
	cout << "area = " << et.area << endl;
}

	/*Note: 
	1)Friendship is not mutual, homework has
	  access to EquilateralTriangle's private and 
	  public members but EquiliateralTriangle does
	  not have access to Homework's members.
	2)A friend function is NOT inherited by a potential
	  child class of EquilateralTriangle 
	3)Friend functions are heavy used in operator over-
	  loading. Remember we used structs to overload last
	  time but if you want to use classes instead, you
	  need to use friend functions to gain access to 
	  private variables.
	*/

};


int main()
{
	EquilateralTriangle et;
	et.setA(3);
	Homework h;

	h.PrintResults(et);

	return 0;	
}