#include <iostream>
#include <string>
using std::endl;
using cout::endl;

namespace gasoline
{
	struct Car
	{
		string Name;
		int TopSpeed = 200, Acceleration = 15;

		Car(string name)
		{
			Name = name;
		}
	};

	ostream& operator<<(ostream& COUT, Car& car)
	{
		COUT << "Name: "<< car.Name << endl;
		COUT << "Top speed: " << car.TopSpeed << endl;
		COUT << "Acceleration: " << car.Acceleration << endl;
		return COUT;
	}
}

namespace electric
{
	struct Car
	{
		string Name;
		int TopSpeed = 150, Acceleration = 30;

		Car(string name)
		{
			Name = name;
		}
	};

	ostream& operator<<(ostream& COUT, Car& car)
	{
		COUT << "Name: "<< car.Name << endl;
		COUT << "Top speed: " << car.TopSpeed << endl;
		COUT << "Acceleration: " << car.Acceleration << endl;
		return COUT;
	}
}

namespace hybrid
{
	struct Car
	{
		string Name;
		int TopSpeed = 170, Acceleration = 25;

		Car(string name)
		{
			Name = name;
		}
	};

	ostream& operator<<(ostream& COUT, Car& car)
	{
		COUT << "Name: "<< car.Name << endl;
		COUT << "Top speed: " << car.TopSpeed << endl;
		COUT << "Acceleration: " << car.Acceleration << endl;
		return COUT;
	}
}

int main()
{
	electric::Car car1 = electric::Car("Tesla");
	hybrid::Car car2 = hybrid::Car("Toyota");
	gasoline::Car car3 = gasoline::Car("Dodge");

	cout << car1 << car2 << car3 << endl;

	return 0;
}