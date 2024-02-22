#include <iostream>
#include <cctype>
using namespace std;

int main()

{
	char c;
	long nChar = 0, nConv = 0;

	while (cin.get(c))  //As long as a character can be read
	{
		++nChar; //increment
		if( islower(c)) //is this a lowercase letter?
		{
			c = toupper(c);  //converts the character
            ++nConv;         //and counts it
		}
		cout.put(c); //outputs the character

		if(c == '%')
			break;
	}

    clog << "\nTotal of character:      " << nChar
         << "\nTotal of converted characters: " << nConv << endl;

    return 0;


}