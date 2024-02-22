//Demonstrate the command line arguments

#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
	if (argc != 4)
	{
		cerr << "Use: hello name1 name2" << endl;
		return 1;
	}

	cout << "Hello " << argv[1] << "!" << endl;
	cout << "Best wishes \n" << "\tyours " << argv[2] << endl;
	cout << argv[3] << endl;

	return 0;
}