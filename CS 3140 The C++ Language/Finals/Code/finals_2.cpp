#include <iostream>
#include <fstream>
using namespace std;
 
float conversion(float celsius)
{
	float sum = celsius + 273.15;
	return sum;
}

int main()
{

    float cel;
	cout << "Convert temperature in Celsius to Kelvin:\n";
	cout << "---------------------------------------------------\n";	
    cout << "Input the temperature in Celsius: ";
    cin >> cel;

	fstream myFile;
	myFile.open("finals_2.txt", ios::out); //write
	if (myFile.is_open())
	{
		myFile << "The temperature in Celsius : " << cel << endl;
    	myFile << "The temperature in Kelvin : " << conversion(cel) << endl;
		myFile << endl;
		myFile.close();
	}
      
    cout << "The temperature in Celsius : " << cel << endl;
    cout << "The temperature in Kelvin : " << conversion(cel) << endl;
	cout << endl;
    return 0;
}