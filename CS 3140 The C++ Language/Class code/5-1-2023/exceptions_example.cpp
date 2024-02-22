#include <iostream>
#include <string>
using namespace std;

class Printer
{
private:
	string _name;
	int _availablePaper;

public:
	Printer(string name, int paper)
	{
		_name = name;
		_availablePaper = paper;
	}

	void print(string txtDoc)
	{
		int requiredPaper = txtDoc.length() / 10;

		if (requiredPaper > _availablePaper)
		{
			throw 50.50;
		}

		cout << "Printing ..." << txtDoc << endl;
		_availablePaper -= requiredPaper;
	}

	int getCurrentPaper()
	{
		return _availablePaper;
	}
};



int main()
{
	Printer myPrinter("HP Dekstop", 10);


	try
	{
		myPrinter.print("Autobiography: From Baller to Teacher.");
		myPrinter.print("Autobiography: From Baller to Teacher.");
		myPrinter.print("Autobiography: From Baller to Teacher.");
		myPrinter.print("Autobiography: From Baller to Teacher.");

		cout << myPrinter.getCurrentPaper() << endl;
	}
	catch(const char * txtException)
	{
		cout << "Expection: " << txtException << endl;
	}
	catch(int exCode)
	{
		cout << "Expection: " << exCode << " . Please contact the administrator for more information." << endl;
	}
	catch(...) //default handler, will handle any type of exception
	{
		cout << "Exception happend. What did you do???" << endl;
	}

	return 0;
}