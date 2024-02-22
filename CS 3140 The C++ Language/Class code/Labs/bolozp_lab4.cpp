/* Lab 4 
 
Write a C++ program that reads a word from the keyboard, stores it in a string,
and checks whether the word is a palindrome.
A palindrome reads the same from left to right as from right to left.
The following are examples of palindromes:“OTTO, ” “deed, ” and “level.”
Use the subscript operator []. 
Modify the program to continually read and check words.*/






















// -----------------------------------------------------
// palindrome.cpp: Reads and compares lines of text.
// -----------------------------------------------------
#include <iostream>
#include <string>
using namespace std;
string header = " * * * Testing palindromes * * * ",
prompt = "Enter a word: ",
line( 50, '-');


int main()
{
	string word; // Empty string
	char key = 'y';
	cout << "\n\t" << header << endl;
	while( key == 'y' || key == 'Y')
	{
		cout << '\n' << line << '\n'
			 << prompt;
		cin >> word;
		// Compares the first and last character,
		// the second and the second to last etc.
		int i = 0, j = word.length() - 1;
		for( ; i <= j ; ++i, --j)
			if( word[i] != word[j] )
				break;
		if( i > j) // All characters equal?
			cout << "\nThe word " << word
				 << " is a P A L I N D R O M E !" << endl;
		else
			cout << "\nThe word " << word
				 << " is not a palindrome" << endl;
		cout << "\nRepeat? (y/n) ";
		do
			cin.get(key);
		while( key != 'y' && key != 'Y'
			   && key != 'n' && key != 'N');
		cin.sync();
	}
	return 0;
}