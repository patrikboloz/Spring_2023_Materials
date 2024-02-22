//Classroom class

#include <iostream>
#include <random>
#include <time.h>
#include <string>
using namespace std;

class Classroom
{
private:
	string name[10] = {"Patrik", "Jeff", "Devyn", "Tyler", "Bob", "Alex", "Chris", "Mario", "Jay", "Luigi"};
	string subjects[5] = {"Math", "Chem", "Biology", "Physics", "English"};
	int grades[5][10];
public:

	void random_grades_generator()
	{
		srand(time(NULL));

		for(int i=0; i<5; i++)
		{
			for (int j=0; j<10; j++)
			{
				grades[i][j] = 1 + (rand() % 100);
			}
		}
	}

	void class_show()
	{
		cout << "Here is a table of all students, subjects, and their grades:\n"
		     << "============================================================\n";

		cout << "\t";

		for (int i=0; i<10; i++)
		{
			cout << name[i] << "\t ";
		}

		cout << endl;

		for (int i=0; i<5; i++)
		{
			cout << subjects[i] << "\t";
			for (int j=0; j<10; j++)
			{
				cout << grades[i][j] << "\t";
			}
			cout << endl;
		}
	}

	float class_average(int choice)
	{
		float sum, average;

		for( int i=0; i<10; i++)
		{
			sum += grades[choice][i];
		}

		average = sum / 10;
		return average;
	}
};