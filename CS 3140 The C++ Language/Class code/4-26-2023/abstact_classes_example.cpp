#include <iostream>
using namespace std;

class Instrument
{
public:
	virtual void make_sound() = 0; //pure virtual function

	//Abstract class in C++ is defined as having at least
	//1 pure virtual function.
};

class Accordion:public Instrument
{
public:
	void make_sound()
	{
		cout << "The accordion is playing." << endl;
	}
};

class Piano:public Instrument
{
public:
	void make_sound()
	{
		cout << "The piano is playing." << endl;
	}
};

int main()
{
	Instrument* i1 = new Accordion();

	//i1->make_sound();

	Instrument* i2 = new Piano();
	//i2->make_sound();

	Instrument* instruments[2] = {i1, i2};
	for (int i=0; i<2 ;i++)
	{
		instruments[i]->make_sound();
	}

	return 0;
}