#include <iostream>
using namespace std;

int main()
{
    float limit, speed, toofast;
    cout << "\nSpeed limit:";
    cin >> limit;
    cout << "\nSpeed:";
    cin >> speed;

    if( (toofast = speed - limit) < 10)
    	cout << "You were lucky!" << endl;
    else if (toofast < 20)
    	cout << "Fine payable: 40 Dollars" << endl;
    else if (toofast < 40)
    	cout << "Fina payable: 120 Dollars" << endl;
    else
    	cout << "Hand over your license, scum!" << endl;

    return 0;


}