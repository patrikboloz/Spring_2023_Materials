#include <iostream>
#include <string>
using namespace std;

class Building
{
protected:
	string name;
	string size;
	int closed, opened;
public:
	Building(string building_name)
	{
		name = building_name;
		size = "Medium";
		opened = 9;
		closed = 5;
	}

	void set_open_hours(int hour)
	{
		opened = hour;
		cout << "The building's opening hour was updated. Now the building opens at: " << opened << endl;
	}

	void set_closed_hours(int hour)
	{
		closed = hour;
		cout << "The building's closing hour was updated. Now the building closes at: " << closed << endl;
	}

	void set_name(string new_name)
	{
		name = new_name;
	}

	string get_name()
	{
		return name;
	}

	string get_size()
	{
		return size;
	}

	int get_open_hours()
	{
		return opened;
	}

	int get_closed_hours()
	{
		return closed;
	}

	void show_info()
	{
		cout << "The buildings name is: " << name << endl;
		cout << "The buildings open hour is: " << opened << endl;
		cout << "The buildings closed hour is: " << closed << endl;
		cout << "The buildings size is: " << size << endl;
		cout << "=======================================" << endl;
	}

};

class Storage:public Building
{
public:

	Storage(string building_name):Building(building_name)
	{
		size = "Big";
		opened = 1;
		closed = 1;
	}
};

class Corner_Store:public Building
{
public:

	Corner_Store(string building_name):Building(building_name)
	{
		size = "Small";
		opened = 8;
		closed = 3;
	}
};

int main()
{
	Building building1("Walmart");
	Storage building2("Amazon Warehouse");
	Corner_Store building3("Abraham's Deli");

	building1.show_info();
	building2.show_info();
	building3.show_info();

	return 0;
}