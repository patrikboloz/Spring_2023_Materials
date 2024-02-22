#include <iostream>
#include <string>
using namespace std;

int main()
{
    void srand(unsigned int seed);
    int rand(); //or int rand(void);

    string s("I am a string");
    cout << "This is the lenght of the s string " 
         << s.length() << endl;
    
    getline(cin, s);
    
    cout << s << endl;

    return 0;
}
