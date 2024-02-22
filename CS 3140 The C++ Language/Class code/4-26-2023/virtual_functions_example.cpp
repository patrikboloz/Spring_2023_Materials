#include <iostream>
using namespace std;

class Instrument
{
public:
	virtual void make_sound()
	{
		cout << "The instrument is playing." << endl;
	}
};

class Accordion:public Instrument
{
public:
	void make_sound()
	{
		cout << "The accordion is playing." << endl;
	}
};

int main()
{
	Instrument* i1 = new Accordion();

	i1->make_sound();

	return 0;
}