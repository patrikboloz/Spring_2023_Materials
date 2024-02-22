#include <iostream>
#include <array>
using namespace std;


int main()
{
	int a[10]; //stack
	a[0] = 50;
	a[1] = 100;
	a[9] = 500;
	//a[20] = 1123;

	cout << a[0] << endl;
	cout << a[1] << endl;
	cout << a[9] << endl;
	//cout << a[20] << endl;

	array<int, 10> b; //standard array
	b[9] = 20;
	b[20] = 500;

	cout << b[20] << endl;

	cout << "size of the b std array is:" << b.size() << endl;
	cout << "the data in std array b is:" << b.data() << endl;

}