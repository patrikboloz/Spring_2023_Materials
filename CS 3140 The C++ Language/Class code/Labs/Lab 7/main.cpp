//Testing of all the methods

#include "classroom.h"

int main()
{
	Classroom A1;
	A1.random_grades_generator();
	A1.class_show();
	cout << "Class average for one subject: " << A1.class_average(1) << endl;

	return 0;
}