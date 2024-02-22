"""Lab 2:
You will create a class called Student with these initial
parameters: first_name, last_name, age, school, major. 
These parameters have to be defined in the __init__ method. 
The methods that the class will have are 
transfer_school, change_major, show. 
You will then create 5 different Student objects with different
starting arguments. Show that your methods are working.
Due by the next lab.
"""

class Student():

    def __init__(self, first_name, last_name, age, school, major):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.school = school
        self.major = major

    def transfer_school(self, transfered_school):
        self.school = transfered_school

    def change_major(self, changed_major):
        self.major = changed_major

    def show(self):
        print("The student's first name is:", self.first_name)
        print("The student's last name is:", self.last_name)
        print("The student's age is:", self.age)
        print("The student's school is:", self.school)
        print("The student's major is:", self.major)
        print()





student_1 = Student("Patrik", "Boloz", 27, "NMHU", "CS")
student_2 = Student("Jeff", "Stokes", 22, "UNM", "Business")

student_1.show()
student_2.show()

student_1.transfer_school("Hogwarts")
student_1.change_major("Math")
student_1.show()

