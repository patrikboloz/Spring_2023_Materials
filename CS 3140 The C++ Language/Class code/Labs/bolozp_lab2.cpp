// Lab 2
// Write a C++ program that by user's input will take 4 numbers the type double and
// calculates their averages. Then you will input a number to be compared to the
// average and it will print out True if the average is bigger (False otherwise). 
// Use the manipulator boolaplha to print out true/false instead of 1/0.
// Lastly input an integer and print out its conversion to dec, oct, and hex
// Due by the end of the Lab

#include <iostream>
#include <iomanip>
using namespace std;

int main()
{ 
    double a, b, c, d, number;
    int conversion;

    cout << "\nPlease enter 4 numbers (could be type double): ";
    cin >> a >> b >> c >> d;

    //Calculate average
    cout << "The average of all 4 numbers is:"
         << ((a + b + c + d)/4) << endl;

    //Input a number and see if the average is bigger

    cout << "Input a number to see if it is bigger than the average of the 4 numbers:"
         << endl;
    cin >> number;    
    cout << "Is the average bigger than the number inputed?\n"
         << boolalpha 
         << (number < (((a + b + c + d)/4))) << endl;   

    //Convert an inputed number into dec, hex, and oct
    cout << "Input an integer to be convereted to dec, hex, and oct form:\n"
         << endl;
    cin >> conversion;

    cout << "\nConversion of the first inputed number into other bases:"
         << "\n decimal:      " << dec << conversion
         << "\n octal:        " << oct << conversion
         << "\n hexadecimal:  " << hex << conversion
         << endl;

    return 0;


}