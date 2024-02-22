#include <iostream>
#include <string>
using namespace std;

class Animal
{
protected:
	int currentHealth;
	int currentFood;
	int currentWater;
	int sleepTime = 8;
	int currentSleepiness;
	string animalType;
public:
	Animal(string animaltype = "Basic")
	{
		if (animaltype == "Basic")
		{
			animalType = animaltype;
			currentHealth = 100;
			currentFood = 100;
			currentWater = 100;
			sleepTime = 8;
			currentSleepiness = 0;
		}
		else
		{
			animalType = animaltype;
		}
	}

	void sleep()
	{
		if (currentSleepiness < sleepTime)
		{
			currentSleepiness = 0;
		}
		else
		{
			currentSleepiness = currentSleepiness - sleepTime;
		}
	}

	void hunt()
	{
		currentSleepiness = currentSleepiness + 5;
		currentHealth = currentHealth - 20;
		currentFood = currentFood + 20;
		currentWater = currentWater - 20;
	}

	void drink()
	{
		currentSleepiness = currentSleepiness + 1;
		currentHealth = currentHealth + 5;
		currentWater = currentWater + 50;
	}

	void make_noise()
	{
		cout << animalType << " makes a sound!" << endl;
	}

	void get_status()
	{
		cout << "This animal is a: " << animalType << endl;
		cout << "It's health is: " << currentHealth << endl;
		cout << "It's current food is: " << currentFood << endl;
		cout << "It's current sleepines is: " << currentSleepiness << endl;
		cout << "It's current water is: " << currentWater << endl;
		cout << endl;
	}
};

class Bird:public Animal
{
public:
	Bird(string animaltype = "Bird"):Animal(animaltype)
	{
		currentHealth = 50;
		currentFood = 50;
		currentWater = 50;
		sleepTime = 5;
		currentSleepiness = 7;
	}

	void make_noise()
	{
		cout << animalType << " chirps!" << endl;
	}

	void hunt()
	{
		currentSleepiness = currentSleepiness + 10;
		currentHealth = currentHealth - 5;
		currentFood = currentFood + 10;
		currentWater = currentWater - 30;
	}
};

int main()
{
	Animal A1;
	Bird B1;

	A1.get_status();
	B1.get_status();

	A1.hunt();
	B1.hunt();

	A1.get_status();
	B1.get_status();

	Animal* pointer_1 = &A1;
	Bird* pointer_2 = &B1;

	pointer_1->sleep();
	pointer_2->sleep();

	pointer_1->get_status();
	pointer_2->get_status();

}