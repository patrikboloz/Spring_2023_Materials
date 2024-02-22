#include <iostream>
using namespace std;

int main()
{
	int a[10]; //Stack
	int* b = new int[10]; //Heap

	a[17] = 6; //VERY BAD, INVALID INDEX

	delete[] b;

	return 0;
}