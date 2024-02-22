#include <iostream>
using namespace std;

int main()
{
	float x, y;

	cout << "Type two different numbers:\n";
	if (cin >> x && cin >> y)
	{
		cout << "\nThe greater value is:"
		     << (x > y ? x : y) << endl;
			
	}
	else
	{
        cout << "\nInvalid input!" << endl;	
	}

	return 0;
}

