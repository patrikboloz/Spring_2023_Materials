#include <iostream>
using namespace std;

class Instrument
{
//Abstract class in C++ is defined as having at least
//one pure virtual function.

public:
	virtual void makeSound() = 0; //pure virtual function

};

class Accordion:public Instrument
{
public:
	void makeSound()
	{
		cout << "The accordion is playing." << endl;
	}
};

class Piano:public Instrument
{
public:
	void makeSound()
	{
		cout << "The piano is playing." << endl;
	}
};


int main()
{
	Instrument* i1= new Accordion();
	//i1->makeSound();

	Instrument* i2= new Piano();
	//i2->makeSound();

	Instrument* instruments[2] = {i1, i2};
	for (int i = 0; i<2; i++)
	{
		instruments[i]->makeSound(); //polymorphism example
	} 

	return 0;
}