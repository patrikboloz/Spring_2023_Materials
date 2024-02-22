// Containing the function cutline(), which removes tabulator characters at 
// the end of the string line. The string line has to be globally defined in 
// another source file.

#include <string>
using namespace std;

extern string line; //extern declaration

void cutline()
{
	int i = line.size(); // Position after the last character

	while (i-- >= 0) //If no blank and no tab, stop the loop
		if (line[i] != ' ' && line[i] != '\t')
			break;

	line.resize(++i); //Fix new length
}