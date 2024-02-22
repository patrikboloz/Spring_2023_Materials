// THe functions getPassword() and timediff() to read and examine a password

#include <iostream>
#include <iomanip>
#include <string>
#include <ctime>
using namespace std;


long timediff(void); //Prototype
static string secret = "ISUS"; // Password
static long maxcount = 3, maxtime = 60; //Limits

bool getPassword() // Enter and check a password, return value true if the password is ok
{
	bool ok_flag = false; // for return value
	string word; //for input
	int count = 0, time = 0;
	timediff(); //To start the stop watch
	while ( ok_flag != true && ++count <= maxcount)
	{
		cout << "\n\nInput the password: ";
		cin.sync(); //clear input buffer
		cin >> setw(20) >> word;
		time += timediff();
		if (time >= maxtime) //Within the time limit
			break;
		if(word != secret)
			cout << "Invalid password!" << endl;
		else
			ok_flag = true; //give permission
	}
	return ok_flag; //result
}

long timediff() //Returns the number of seconds after the last call
{
	static long sec = 0; //Time of last call.
	long oldsec = sec; //Saves previous time
	time(&sec); //Reads new time.
	return (sec - oldsec); //Returns the difference
}

int main()
{
	getPassword();
	return 0;
}