#include <iostream>
using namespace std;

int factorial(int a)
{
	int factorial=1;
	for (int i=1; i<=a; i++)
	{
		factorial = factorial * i;
	}
	return factorial;
}


int main()
{
	int number;

	cout << "Please input a number between 0 and 50:" << endl;
	cin >> number;
	if (number < 0)
	{
		cout << "Number was negative, can't perform calculation." << endl;
	}
	else if (number > 10)
	{
		cout << "Number was bigger than 10, can't perform calculation." << endl;
	}
	else
	{
		cout << "The factorial of your number " << number <<" is: " << factorial(number) << endl;
	}

	return 0;
}
