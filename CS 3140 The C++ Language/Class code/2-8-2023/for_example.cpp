#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	int count = 1; //Initialization
    while (count <= 10) //Controlling expression
    {
    	cout << count
    	     << ". loop" << endl;
    	++count; //Reinitialization
    }

    int count_b;
    for (count_b = 1; count_b <= 10; ++count_b)
    {
    	cout << count_b
    	     << ". loop" << endl;
    }

    for (int i = 0; i < 25; cout << "\n" << i++)
    	;

    int x, a, limit;
    for (a=0, limit=8; a < limit; a += 2)
    {
    	x = a * a, cout << setw(10) << x;
    } 


	return 0;
}