//Defines and calls the function reverse()
//reverse() copies a C string into another C string and reverses the order of characters


#include <iostream>
#include <string.h>
using namespace std;

void reverse( char str[], char umstr[]);

int main()
{
	const int CNT = 81;
	char word[CNT], revword[CNT];

	cout << "Enter a word: ";
	cin.width(CNT);
	cin >> word;

	reverse(word, revword);

	cout << "\nThe \"reversed\" word:   " << revword << endl;

	return 0;
}

void reverse( char s1[], char s2[])
{
	int j = 0;

	for (int i = strlen(s1)-1; i >= 0; i--, j++)
		s2[j] = s1[i];

	s2[j] = '\0';

}