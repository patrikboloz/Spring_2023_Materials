#include <iostream>
//using namespace std;
using std::cout;
using std::endl;

//Why namespace std is bad?
//std has many objects in library that when creating
//own functions, they can overlap with other objects in
//std that can cause collisions and so on.

namespace namespace1
{
	int age = 25;
	std::string name = "Patrik";
}

namespace namespace2
{
	int age = 26;
}

int main()
{
	cout << namespace2::age << endl;
	cout << namespace1::name << endl;

	return 0;
}