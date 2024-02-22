#include "account.h"

int main()
{
	Account temp2;
    temp2.display();

    temp2.setState(500000);
    cout << temp2.getState() << endl;

    return 0;

}