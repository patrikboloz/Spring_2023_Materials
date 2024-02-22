
//Testing of all the methods

#include "classroom.h"


int main()
{
	Classroom A1;
	A1.random_grades_generator();
	A1.class_show();
	cout << A1.class_average(0) << endl;

	return 0;

}