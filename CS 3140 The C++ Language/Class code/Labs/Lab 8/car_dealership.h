#include <iostream>
#include <string>
#include <random>
#include <time.h>
using namespace std;

class Car_Dealership
{
private:
	string car_bodytype[5] = {"Sedan", "Pickup", "MV", "SUV", "Conver"};
	string car_type[3] = {"Ford", "Chevy", "Ferrari"};
	string availability_choice[2] = {"Yes","No"};
	string availability[3][5];
	

	int random_index;

public: 
	void car_availability()
	{
		srand ( time(NULL) );
		

		for (int i = 0; i < 3; i++)
		{
			for (int j = 0; j < 5; j++)
			{
				random_index = rand() % 2;
				availability[i][j] = availability_choice[random_index];

			}
		} 
	}

	void current_stock()
	{
		cout << "\t|";
		for (int i = 0; i < 5; i++)
		{
				cout << car_bodytype[i] << "\t|";
		}

		cout << endl;
		for (int i = 0; i < 3; i++)		
		{
			cout << car_type[i] << "\t|";

			for (int j = 0; j < 5; j++)
			{
				cout << availability[i][j] << "\t|";
			}
			cout << "\n";
		} 
	}

	void new_day()
	{
		car_availability(); //generating new stock

		cout << "\t|";
		for (int i = 0; i < 5; i++)
		{
				cout << car_bodytype[i] << "\t|";
		}

		cout << endl;
		for (int i = 0; i < 3; i++)		
		{
			cout << car_type[i] << "\t|";

			for (int j = 0; j < 5; j++)
			{
				cout << availability[i][j] << "\t|";
			}
			cout << "\n";
		} 

	}

	bool user_choice(int bodytype_choice, int type_choice)
	{
		if (availability[type_choice][bodytype_choice] == "Yes")
		{
			return true;
		}
		else
		{
			return false;
		}
	}
};