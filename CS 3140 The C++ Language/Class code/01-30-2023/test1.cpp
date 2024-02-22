#include <iostream>
#include <cmath>
using namespace std;

// Calculating powers with the standard
// function pow()


int main()
{
    double x = 2.5, y;
    
    // By means of a prototype, the compiler generates
    // the correct call or an error message!
    
    // Computes x raised to the power of 3:
    //y = pow("x", 3.0);  //Error! String is not number
    //y = pow(x + 3.0); // Error! Just one argument
    y = pow(x , 3.0); // ok!
    y = pow(x , 3); // ok!
    
    cout << "2.5 raised to 3 yields: "
         << y << endl;
         
    // Calcualting with pow() is possible:
    cout << "2 + (5 raised to the power 2.5) yields: "
         << 2.0 + pow(5.0, x) << endl;


    return 0;
}


