#include <iostream>
#include <string>
using namespace std;

struct Classroom //constructs attributes are public on default
{
	string StudentName = "Patrik";
};

class Classroom2 //classes attributes are private on default
{
public:
	string StudentName = "Jeff";

	void setName(string newStudent)
	{
		StudentName = newStudent;
	}
};

int main()
{
	Classroom A;
	Classroom2 B;

	//cout << A.StudentName << endl;
	cout << B.StudentName << endl;
	B.setName("Bob");
	cout << B.StudentName << endl;
}