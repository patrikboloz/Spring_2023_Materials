#include <iostream>
using namespace std;

int main()
{
    //int a(4); double x(7.9);
    //a * 512; //type int
    //1.0 + sin(x);  //type double
    //x - 3; //double, since one operand is of type double
    //2 + 7*3 //23
    //(2 + 7)*3 //27

    int i(5), j(8);
    cout << i++ << endl;
    cout << i << endl;
    cout << j-- << endl;
    cout << --j << endl;

    float val(5.0); 
    cout << ++val - 7.0/2.0 << endl;

    double z = 7.5;
    double y = z;
    double x = 2.0 + 4.2 * z;
    cout << x << endl;

    //sin(x = 2.5);

    //int h = k = 9;

    int o;
    o += 3;
    cout << o << endl;

    //length == circuit 

    cout << ('A' < 'a') << endl; //'A' is 65, 'a' is 97

    double index(50), max(20);
    bool flag = index < max - 1;
    cout << flag << endl;

    int result;
    (result = index + 1) == max;
    cout << result << endl;

    cout << ((index < 0.2) || (index > 9.8)) << endl;
    cout << ((index <= 50) && (index > 9.8)) << endl;

    int v(7);
    cout << (v++ == 8 || v == 7) << endl;



}