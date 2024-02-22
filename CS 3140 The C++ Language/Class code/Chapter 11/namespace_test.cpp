#include <iostream>
//using namespace std;

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
	std::cout << namespace2::age << std::endl;
	std::cout << namespace1::name << std::endl;

	return 0;
}