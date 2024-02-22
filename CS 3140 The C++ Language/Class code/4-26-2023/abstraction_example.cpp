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
		cout << "Android is capturing video.." << endl;
	}

	void MakeACall()
	{
		cout << "Android is making a call..." << endl;
	}	
};

class IPhone:public Smartphone
{
public:
	void VideoCapture()
	{
		cout << "IPhone is capturing video..." << endl;
	}

	void MakeACall()
	{
		cout << "IPhone is making a call..." << endl;
	}
};

int main()
{
	Smartphone* s1 = new Android();
	s1->MakeACall();

	Smartphone* s2 = new IPhone();
	s2->VideoCapture();

	return 0;
}