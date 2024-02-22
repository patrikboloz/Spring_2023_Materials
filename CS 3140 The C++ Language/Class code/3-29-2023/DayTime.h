//The class DayTIme represent the time in hours, minutes, and seconds
#include <ctime>
#include <iostream>
using namespace std;

class DayTime
{
private:
	short hour, minute, second;
	bool overflow;

public:
	DayTime(int h = 0, int m = 0, int s = 0)
	{
		overflow = false;
		if (!setTime(h, m, s))
			hour = minute = second = 0;
	}
	bool setTime(int hour, int minute, int second = 0)
	{
		if (hour >= 0 && hour < 24
			&& minute >= 0 && minute < 60
			&& second >= 0 && second < 60)
		{
			this->hour = (short)hour;
			this->minute = (short)minute;
			this->second = (short)second;
			return true;
		}
		else
			return false;
	}

	int getHour() const {return hour;}
	int getMinute() const {return minute;}
	int getSecond() const {return second;}

	int asSeconds() const // daytime in seconds
	{return (60*60*hour + 60*minute + second);}

	bool isLess (DayTime t) const // compare *this and t
	{
		return asSeconds() < t.asSeconds(); //this->asSeconds() < t.asSeconds();
	}

};

const DayTime& currentTime() //Return the present time
{
	static DayTime curTime;
	time_t sec; time(&sec); //Gets the present time
	struct tm *time = localtime(&sec);
	curTime.setTime( time->tm_hour,
		             time->tm_min,
		             time->tm_sec);
	return curTime;
}
