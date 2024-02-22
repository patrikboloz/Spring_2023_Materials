#include "greatest.h"
#include "student.h"
#include "rectangle.h"

//1) Write a C++ Program to find Largest among 3 numbers using classes
//2) Write a class having two private variables and one member function 
//   which will return the area of the rectangle.
//3) Write a c++ class called 'student' with data members

//   name(char type),
//   midterm_grade,final_grade (double type)

//   The program asks the user to enter name and grades. Then calc_average() 
//   calculates the average grade and disp() display name and the average grade 
//   on screen in different lines.












int main()
{
	//=========1===========
	greatest g;
    g.input();
    g.calc();

    //=========2===========

    rectangle rect;
    cout<<"Enter length of rectangle:"<< endl;
    cin>>rect.x;
    cout<<"Enter width of rectangle:"<< endl;
    cin>>rect.y;
    cout <<"Area:"<< rect.area() << endl;


    //=========3===========
	char* nam;int m1,m2;

	cout << "Enter name:" << endl;
	cin>> nam;
	cout << "Enter marks of two subjects:" << endl;
	cin>> m1;
	cin>> m2;

	Student student1(nam,m1,m2);
	student1.disp();


}