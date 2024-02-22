#include "car_dealership.h"

int main()
{
	int general_choice, car_choice1, car_choice2;
	Car_Dealership SantaFe;

	SantaFe.car_availability();

	while (true)
	{
		cout <<  "\n=================================================================\n"
		   		 "Welcome to Santa Fe Dealrship, where we will try to sell you a car\n"
		         "with 20.000 miles for $5000 more than the new car price! Welcome!\n"
		         "=================================================================\n"
		         "Please choose what would you like to do:\n"
		         "1) See today's stock of all cars.\n"
		         "2) See a specific stock of a certain car. \n"
		         "3) Go to a new day.\n"
		         "4) Leave the dealership.\n";

		cin >> general_choice;
		cout << "\033[2J\033[1;1H";

	
		if (general_choice == 1)
		{
			cout << "This is today's stock:\n";
			SantaFe.current_stock();
		}
		else if (general_choice == 3)
		{
			cout << "It's a new day which means new stock!\n";
			SantaFe.new_day();
		}
		else if (general_choice == 4)
		{
			cout << "Cya!\n";
			exit(0);
		}
		else if (general_choice == 2)
		{
			cout << "\033[2J\033[1;1H";
			cout << "Please choose a body first:\n"
			         "1) Sedan\n"
			         "2) Pickup\n"
			         "3) Minivan\n"
			         "4) SUV\n"
			         "5) Convertible\n"
			         "And then choose the car type:\n"
			         "1) Ford\n"
			         "2) Chevy\n"
			         "3) Ferrari\n";

			cin >> car_choice1 >> car_choice2;
			if (SantaFe.user_choice(car_choice1 - 1, car_choice2 - 1))
				{cout << "Your chosen car is in stock! Want our financing with huge interest rate?\n";}
			else
				{cout << "Your car ain't in stock. Maybe try another day!\n";}

			cout << "Going back to main menu...\n\n";

		}
	}

	return 0;

}