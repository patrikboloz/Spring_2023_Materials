#include <iostream>
#include <vector>
#include <list>
#include <deque>
#include <set>
#include <unordered_set>

#include <map>
#include <unordered_map>

#include <algorithm>
#include <chrono>
#include <string>
using namespace std;

void map_example()
{
	map<string, int> container;
		
	container["five"] = 5;
	container["six"] = 6;
	container["three"] = 3;
	container["four"] = 4;
	container["two"] = 2;
	container["one"] = 1;

	for (auto& i : container)
	{
		cout << i.first << " = " << i.second << endl;
	}
}

void container_example()
{
	//Lamba function to roll a die
	auto roll = []() {return rand() % 6 +1; };

	//Create a container
	vector<int> container; 
	//list<int> container; //doubly linked list
	//deque<int> container; //double ended queue
	//set<int> container; // ordered set
	//unordered_set<int> container; // unordered set


	//Add 1 item
	container.push_back(roll());
	//container.insert(roll()); //for sets


	const int* pAddressOfOriginalItemZero = &(*container.begin());

	chrono::duration<double> durInsertTime(0);

	do
	{
		// Get address of first item
		const int* pAddressOfItemZero = &(*container.begin());

		cout << "Contains " << container.size() << " elements, took " 
		     << chrono::duration_cast<chrono::microseconds>(durInsertTime).count() << " microseconds\n";

		for (const auto& i : container)
		{
			const int* pAddressOfItemX = &i;
			int pItemOffset = pAddressOfItemX - pAddressOfItemZero;
			int pItemOffsetOriginal = pAddressOfItemX - pAddressOfOriginalItemZero;
			cout << "Offset from original: " << pItemOffsetOriginal 
			     << "  Offset from zero: " << pItemOffset 
			     << "  :  Content: " << i << endl;
		}

		auto tp1 = chrono::high_resolution_clock::now();
		
		container.push_back(roll());
		//container.insert(roll()); // for sets
		
		auto tp2 = chrono::high_resolution_clock::now();
		durInsertTime = (tp2 - tp1);

	} while (getc(stdin));

}

int main()
{

	container_example();
	//map_example();

	return 0;
}