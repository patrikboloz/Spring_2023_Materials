#include <iostream>
#include <climits>  //Definition of INT_MIN, ...
using namespace std;


int main()
{
    cout << "Range of types int and unisgned int" 
         << endl << endl;
         
    cout << "Type              Minimum             Maximum"
         << endl
         << "---------------------------------------------"
         << endl;
         
    cout << "int               " << INT_MIN << "          "
                                 << INT_MAX << endl;
    cout << "unsigned int      " << "     0               "
                                 << UINT_MAX << endl;
    cout << sizeof(float) << endl;
    cout << sizeof(int) << endl;
    
    
    return 0;
}
