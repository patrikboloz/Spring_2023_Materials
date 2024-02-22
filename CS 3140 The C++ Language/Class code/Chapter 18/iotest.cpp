#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	fstream myFile;
	myFile.open("test.txt", ios::out); //write
	if (myFile.is_open())
	{
		myFile << "Hello\n";
		myFile.close();
	}

	myFile.open("test.txt", ios::app); //append
	if (myFile.is_open())
	{
		myFile << "Append test\n";
		myFile.close();
	}

	return 0;
}