#include <iostream>
using namespace std;

class Instrument
{
public:
	virtual void makeSound()
	{
		cout << "The instrument is playing." << endl;
	}
};

class Accordion:public Instrument
{
public:
	void makeSound()
	{
		cout << "The accordion is playing." << endl;
	}
};


int main()
{
	Instrument* i1= new Accordion();

	i1->makeSound();

	//Virtual functions take the most recent derived function
	//and uses that one. If Accordion's makeSound is not 
	//implemented, then the base Instrument makeSound method 
	//is invoked.

	return 0;
}