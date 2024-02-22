// Interactive environment using the classroom.h class

#include "classroom.h"

int main()
{
	Classroom A1;
	int action;

	A1.random_grades_generator();

	while (true)
	{
		
		cout << "===========================================================================\n"
		     << "Welcome to your classroom grade table. Please choose the following actions.\n"
	         << "1) Generate new grades for your class.\n"
	         << "2) Print your current grades of your class.\n"
	         << "3) Calculate an average class grade of a chosen subject.\n"
	         << "4) End the program.\n"
	         << "===========================================================================\n";

	    cin >> action;
	    cout << "\033[2J\033[1;1H";

	    if (action == 1)
	    {
	    	cout << "Generating new grades, please wait...\n";
	    	A1.random_grades_generator();
	    	cout << "New grades have been generated. Going back to the main menu...\n\n";
	    }
	    else if (action == 2)
	    {
	    	A1.class_show();
	    	cout << "\nGoing back to the main menu...\n\n";
	    }
	    else if (action == 3)
	    {
	    	int action2;

	    	cout << "\033[2J\033[1;1H";
	    	cout << "Choose the subject of which you'd like to get a class average:\n"
	    	     << "1) Math\n" << "2) Chemistry\n" << "3) Biology\n" << "4) Physics\n" << "5) English\n" << endl;

	    	cin >> action2;

	    	if (action2 == 1) 
	    	{
	    		cout << "Printing out the average of the subject Math...\n"
	    		     << "Average is: " << A1.class_average(0);
	    		cout << "\nGoing back to the main menu...\n\n";
	    	}
	    	else if (action2 == 2)
	    	{
	    		cout << "Printing out the average of the subject Chemistry...\n"
	    		     << "Average is: " << A1.class_average(1)<< endl;
	    		cout << "\nGoing back to the main menu...\n\n";
	    	}
	    	else if (action2 == 3)
	    	{
	    		cout << "Printing out the average of the subject Biology...\n"
	    		     << "Average is: " << A1.class_average(2)<< endl;
	    		cout << "\nGoing back to the main menu...\n\n";
	    	}
	    	else if (action2 == 4)
	    	{
	    		cout << "Printing out the average of the subject Chemistry...\n"
	    		     << "Average is: " << A1.class_average(3) << endl;
	    		cout << "\nGoing back to the main menu...\n\n";
	    	}
	    	else if (action2 == 5)
	    	{
	    		cout << "Printing out the average of the subject Chemistry...\n"
	    		     << "Average is: " << A1.class_average(4)<< endl;
	    		cout << "\nGoing back to the main menu...\n\n";
	    	}
	    	else {cout << "Not a valid action, going back to the main menu...\n";}	    	
	    }


	    else if (action == 4)
	    {cout << "Exiting the program. Cya!\n"; exit(0);}
	    
	    else {cout << "Not a valid action, please try again...\n";}
	    
	}


	return 0;

}