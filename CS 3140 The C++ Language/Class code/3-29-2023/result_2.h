//Class Result to represent a measurement and the time of measurement
//Version 2

#include "DayTime.h"

class Result
{
private:
	double val;
	const DayTime time;
public:
	Result(); //Default constructor
	Result(double w, const DayTime& z = currentTime());
	Result(double w, int hr, int min, int sec);

	double getVal() const {return val;}
	void setVal(double w) {val = w;}

	const DayTime& getTime() const {return time;}
	void setTime(const DayTime& z) {time = z;}
	bool setTime(int hr, int min, int sec)
	{return time.setTime(hr, min, sec);}
	void print() const
	{
		cout << "Time: " << time.getHour() << " " 
		                 << time.getMinute() << " " 
		                 << time.getSecond() << endl;
		cout << "Temperature: " << getVal() << endl; 	
	} //Output result and time

};

Result::Result() { val = 0.0;}
Result::Result(double w, const DayTime& z)
{
	val = w;
	time = z;
}
Result::Result(double w, int hr, int min, int sec)
{
	val = w;
	time = DayTime(hr, min, sec); 
}