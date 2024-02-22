#include <iostream>
#include <list>
using namespace std;

class YouTubeChannel
{
private:
	string Name;
	//string OwnerName;
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
		 cout << "Owner's Name: " << OwnerName << endl;
		 cout << "Subscribers count: " << SubscribersCount << endl;
		 cout << "Videos: " << endl;
		 for (string videoTitle : PublishedVideoTitles)
		 {
		 	cout << videoTitle << endl;
		 }
	}

	void PublishVideo(string title)
	{
		PublishedVideoTitles.push_back(title);
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
};

class CookingYouTubeChannel:public YouTubeChannel
{
public:
	CookingYouTubeChannel(string name, string ownername):YouTubeChannel(name, ownername)
	{}

	void Practice()
	{
		cout << OwnerName << " practicing cooking, learning new recipes, and so on..." << endl;
	}
};


int main()
{
	YouTubeChannel P_MLG("PatricksSickMLGCompilations", "Patrik");
	CookingYouTubeChannel P_Cooking("Patrik's Cooking Channel", "Patrik");
	CookingYouTubeChannel B_Cooking("Bob's Cooking Channel", "Bob");


	P_MLG.PublishVideo("Sick COD outplay Compilation 1.");
	P_MLG.Subscribe();
	P_MLG.Subscribe();
	P_MLG.GetInfo();

	P_Cooking.PublishVideo("How to boil eggs.");
	P_Cooking.PublishVideo("How not to overboil eggs.");
	P_Cooking.Subscribe();
	P_Cooking.Subscribe();
	P_Cooking.Subscribe();
	P_Cooking.Unsubscribe();
	P_Cooking.GetInfo();
	P_Cooking.Practice();

	B_Cooking.Practice();

	return 0;
}