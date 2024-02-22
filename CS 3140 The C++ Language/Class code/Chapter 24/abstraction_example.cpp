#include <iostream>
using namespace std;

class Smartphone
{
public:
	virtual void VideoCapture() = 0;
	virtual void MakeACall() = 0;
};

class Android:public Smartphone
{
public:
	void VideoCapture()
	{
		cout << "Android is capturing video..." << endl;
	}
};

class IPhone:public Smartphone
{
public:
void VideoCapture()
	{
		cout << "IPhone is capturing video..." << endl;
	}
};

int main()
{	
	Smartphone* s1 = new Android();
	s1->VideoCapture();

	/* Imagine three developers working on this program
	   The first works on android, the second on Iphone,
	   and third on the main. All developers do not need
	   to know the implementation of each other's program,
	   only need to know what is required.
	   = true abstraction */

	return 0;
}
