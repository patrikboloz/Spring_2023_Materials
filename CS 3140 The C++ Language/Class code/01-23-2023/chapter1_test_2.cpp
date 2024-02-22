/******************************************
A program with some functions and comments
**********************************************/

#include <iostream>
using namespace std;

void line(), message();       //Protypes

int main()
{
    cout << "Hello! The programs starts in main()."
        << endl;
    line();
    message();
    line();
    cout << "At the end of main()." << endl;
   
    return 0;
}

void line()        //To draw a line
{
   cout << "---------------------" << endl;
}

void message()         // To display a message
{
   cout << "In function message()." << endl;
}
