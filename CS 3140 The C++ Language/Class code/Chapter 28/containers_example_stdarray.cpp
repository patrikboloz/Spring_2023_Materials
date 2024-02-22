#include <iostream>
#include <array>
using namespace std;

int main()
{
	int a[10]; //Stack
	//a[17] = 6;

	array<int, 10> b;
	b[17] = 6;

	b.size();
	b.data();

	//

	cout << b << endl;

	return 0;
}