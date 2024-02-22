#include <iostream>
//using namespace std;

//WHy namespace std is bad?
//std has many objects in library that when creating own functions,
//they can overlap with other objects in std that can cause collisions.


namespace namespace1
{
	int age = 25;
	std::string name = "Patrik";
}

namespace namespace2
{
	int age = 69;
}


int main()
{

	std::cout << namespace1::age << std::endl;
	std::cout << namespace2::age << std::endl;

	return 0;
}