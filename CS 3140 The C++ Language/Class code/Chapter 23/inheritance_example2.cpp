#include <iostream>
#include <list>
using namespace std;

class YouTubeChannel
{
private:
	string Name;
	//string OwnerName; moved to protected
	int SubscribersCount;
	list<string> PublishedVideoTitles;

protected:
	string OwnerName;

public:
	YouTubeChannel(string name, string ownername)
	{
		Name = name;
		OwnerName = ownername;
		SubscribersCount = 0;
	}
	void GetInfo()
	{
		cout << "Name: " << Name << endl;
		cout << "OwnerName: "<< OwnerName << endl;
		cout <<	"SubscribersCount: " << SubscribersCount << endl;
		cout << "Videos: " << endl;
		for (string videoTitle : PublishedVideoTitles)
		{
			cout << videoTitle << endl;
		}
	}
	void Subscribe()
	{
		SubscribersCount++;
	}
	void Unsubscribe()
	{
		if(SubscribersCount>0)
			SubscribersCount--;
	}
	void PublishVideo(string title)
	{
		PublishedVideoTitles.push_back(title);
	}

};

class CookingYoutubeChannel:public YouTubeChannel
{
public:
	CookingYoutubeChannel(string name, string ownername):YouTubeChannel(name, ownername)
	{}
	void Practice()
	{
		cout << OwnerName << " practicing cooking, learning new recipes, and so on..." << endl;
	}
};

int main()
{
	YouTubeChannel P_MLG("PatriksSickMLGCompilations", "Patrik");
	CookingYoutubeChannel P_Cooking("Patriks Cooking Channel", "Patrik");
	CookingYoutubeChannel B_Cooking("Bob's Cooking", "Bob");

	P_MLG.PublishVideo("Sick COD outplay Compilation 1.");
	//P_MLG.Practice(); //NOT GOING TO WORK!
	P_MLG.GetInfo();

	P_Cooking.PublishVideo("Goulash.");
	P_Cooking.PublishVideo("Suaerkraut Soup.");
	P_Cooking.Subscribe();
	P_Cooking.Subscribe();
	P_Cooking.Subscribe();
	P_Cooking.GetInfo();
	P_Cooking.Practice();

	B_Cooking.Practice();
	return 0;

}