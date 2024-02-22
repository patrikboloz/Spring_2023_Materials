#include <iostream>
#include <string>
using namespace std;

class Animal
{
protected:
	int currentHealth, currentFood, currentWater, currentSleepiness;
	int sleepTime = 8;
	string animalType;

public:
	Animal(string animaltype= "Basic")
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
		currentWater = currentWater + 50;
		currentHealth = currentHealth + 5;
	}

	void make_noise()
	{
		cout << animalType << " makes a sound!" << endl;
	}

	void get_status()
	{
		cout << "This animal is a " << animalType << endl;
		cout << "It's health is " << currentHealth << endl;
		cout << "It's current food is " << currentFood << endl;
		cout << "It's current sleepiness is " << currentSleepiness << endl;
		cout << "It's current water is " << currentWater << endl;
		cout << endl;
	}
};

class Bird:public Animal
{
public:
	Bird(string animaltype="Bird"):Animal(animaltype)
	{
		currentHealth = 50;
		currentFood = 50;
		sleepTime = 5;
		currentSleepiness = 7;
	}

	void make_noise()
	{
		cout << animalType << " chirps." << endl;
	}
};

int main()
{
	Animal Tiger;
	Bird Parrot;

	Tiger.get_status();
	Parrot.get_status();

	Tiger.make_noise();
	Parrot.make_noise();

	Animal* pointer1 = &Tiger;
	Bird* pointer2 = &Parrot;

	pointer1->sleep();
	pointer2->sleep();

	pointer1->get_status();
	pointer2->get_status();

	return 0;
}