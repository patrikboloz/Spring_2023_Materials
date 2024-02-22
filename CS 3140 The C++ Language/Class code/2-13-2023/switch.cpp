// Evaluates given input.

#include <iostream>
using namespace std;

int command = menu(); // the frunction menu() read a command

switch(command) //evaluate command
{

    case 'a':
    case 'A':
    			action1(); //Carry out 1st action
    			break;
    case 'b':
    case 'B':
    			action2(); //Carry out 2nd action
    			break;
    default:
    			cout << '\a' << flush; //Beep on invalid input

} 