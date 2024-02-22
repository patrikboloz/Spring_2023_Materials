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
		// 40/10 = 4 so we need 4 paper to print this document

		if (requiredPaper > _availablePaper)
		{
			throw 101.0;
			//return; This is redundant, no need to call it since
			//throw already stops the exectution of the function.
		}

		cout << "Printing ..." << txtDoc << endl;
		_availablePaper -= requiredPaper;
	}
};


int main()
{

	Printer myPrinter("HP Desktop", 10);

	try
	{
		myPrinter.print("Hello my name is Patrik. I used to be a damn good baller.");
		myPrinter.print("Hello my name is Patrik. I used to be a damn good baller.");
		myPrinter.print("Hello my name is Patrik. I used to be a damn good baller.");
	}
	/*catch(...) //default handler, will handle any type of exception
	{
		cout << "Exception happened." << endl;
	}*/ //Default handlers are supposed to come LAST!
	catch(const char * txtException)
	{
		cout << "Exception: " << txtException << endl;
	}
	catch(int exCode) 
	{
		cout << "Exception: " << exCode << endl;
	}
	catch(...) //default handler, will handle any type of exception
	{
		cout << "Exception happened." << endl;
	}

	return 0;
}