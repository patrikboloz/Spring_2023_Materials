#include <iostream>
#include <string>
#include <list>
using namespace std;

class Hotel
{
private:
	string name;
	int num_guests = 0;

public:
	Hotel(string hotel_name)
	{
		name = hotel_name;
	}

	void add_guest(string guest_name)
	{
		num_guests += 1;
		cout << "The guest named " << guest_name << " has been succesfully checked in. Welcome!" << endl;		
	}

	void check_out_guest(string guest_name)
	{
		num_guests -= 1;
		cout << "The guest named " << guest_name << " has been succesfully checked out. Good bye!" << endl;	
	}

	int get_numberOfGuests()
	{
		
		return num_guests;
	}

};	

int main()
{
	Hotel hotel("Hilton");

	hotel.add_guest("Patrik");
	hotel.add_guest("Billy");
	hotel.add_guest("Jeff");
	hotel.add_guest("Jonah");

	cout << "The current number of guests is: " << hotel.get_numberOfGuests() << endl;

	hotel.check_out_guest("Jonah");

	cout << "The current number of guests is: " << hotel.get_numberOfGuests() << endl;

	return 0;
}
