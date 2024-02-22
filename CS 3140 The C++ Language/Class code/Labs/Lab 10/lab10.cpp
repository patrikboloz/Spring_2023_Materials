#include <iostream>
#include <string>
using namespace std;


class Full_Employee
{
protected:
	string Name, Title;
	int year_salary;
	bool full_time = true;
public:
	Full_Employee(string name, string title)
	{
		Name = name;
		Title = title;
		year_salary = 50000;
		full_time = true;
	}

	string get_Name()
	{
		return Name;
	}

	string get_Title()
	{
		return Title;
	}

	void set_Salary(int number)
	{
		year_salary = number;
	}

	int get_Salary()
	{
		return year_salary;
	}

	bool set_Status(string status)
	{
		if (status == "Full time")
		{
			return full_time = true;
		}
		else if (status == "Part time")
		{
			return full_time = false;
		}
	}

	void get_Info()
	{
		cout << "Employee's name: " << Name << endl;
		cout << "Employee's title: " << Title << endl;
		cout << "Full time? " << full_time << endl;
		cout << "Year salary: " << year_salary << endl;
	}

};

class Part_Employee:public Full_Employee
{
public:
	Part_Employee(string name, string title):Full_Employee(name, title){
		full_time = false;
		year_salary = 20 * 2 * 15 * 26;
	}
	void set_Salary(int number)
	{
		year_salary = 20 * 2 * number * 26;
	}
};


int main()
{
	Full_Employee F1("Patrik", "Instructor");
	Part_Employee P1("Jeff", "Lab Manager");

	F1.get_Info();
	P1.get_Info();

	return 0;

}