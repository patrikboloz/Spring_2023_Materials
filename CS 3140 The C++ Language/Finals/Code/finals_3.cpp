#include <iostream>
#include <string>
#include <random>
#include <ctime>

using std::endl;
using std::cout;
using std::cin;
using std::string;


void weather_report(string name)
{
	srand(time(0));
	int randIndex = rand() % 4;
	string weatherArray[4] = {"Cloudy", "Sunny", "Rainy", "TORNADOES EVERYWHERE!"};

	cout << "Good morning " << name << endl;
	cout << "Today's weather will be: " << weatherArray[randIndex] << endl;
}

int main()
{
	string name;
	cout << "Please insert your name: " << endl;
	cin >> name;
	weather_report(name);

	return 0;
}