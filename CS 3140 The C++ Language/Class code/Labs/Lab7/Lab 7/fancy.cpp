// Interactive enviornemnt using the classroom.h class

#include "classroom.h"

int main()
{
	Classroom A1;
	int action;
	
	A1.random_grades_generator();

	while (true)
	{
		cout << "=============================================\n"
		     << "Welcome to your classroom grade table. Please choose from the following:\n"
		     << "1) Generate new grades for your class.\n"
		     << "2) Print out your current grades of your class.\n"
		     << "3) Calculate an average class grade of a chosen subject.\n"
		     << "4) Exit the program.\n"
		     << "=============================================\n";

		cin >> action;
		cout << "\033[2J\033[1;1H";

		if (action == 1)
		{
			cout << "Generating new grades, please wait...\n";
			A1.random_grades_generator();
			cout << "New grades have been generated, going back to the main menu.\n\n";

		}
		else if (action == 2)
		{
			A1.class_show();
			cout << "\nGOing back to the main menu...\n\n";
		}

		else if (action == 3)
		{
			int action2;
			cout << "Choose the subject of which you'd like to get a class average:\n"
			     << "1) Math\n" << "2) Chemistry\n" << "3) Biology\n" << "4) Physics\n" << "5) Enlgish\n\n";

			cin >> action2;

			cout << "\033[2J\033[1;1H";

			if (action2 == 1)
			{
				cout << "Average of the subject Math is: " << A1.class_average(0);
				cout << "\nGoing back to the main menu...\n";
			} 
			else if (action2 == 2)
			{
				cout << "Average of the subject Chemistry is: " << A1.class_average(1);
				cout << "\nGoing back to the main menu...\n";
			}
			else if (action2 == 3)
			{
				cout << "Average of the subject Biology is: " << A1.class_average(2);
				cout << "\nGoing back to the main menu...\n";
			}
			else if (action2 == 4)
			{
				cout << "Average of the subject Physics is: " << A1.class_average(3);
				cout << "\nGoing back to the main menu...\n";
			}
			else if (action2 == 5)
			{
				cout << "Average of the subject English is: " << A1.class_average(4);
				cout << "\nGoing back to the main menu...\n";
			}
			else {
				cout << "Wrong choice dumbass, going back to the main menu since you can't behave...\n";
			}		

		}

		else if (action == 4)
		{
			cout << "Exiting out of the program. Cya!\n"; 
			exit(0); 
		}

		else
		{
			cout << "Wrong choice dumbass, going back to the main menu since you can't behave...\n";
		}
	}
	return 0;
}