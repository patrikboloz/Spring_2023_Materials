#Define the Employee class, which we will use as a base/parent class

class Employee():

	def __init__(self, name, title, ratePerHour = None):
		self.name = name
		self.title = title
		if ratePerHour is not None:
			ratePerHour = float(ratePerHour)
		self.ratePerHour = ratePerHour

	def getName(self):
		return self.name

	def getTitle(self):
		return self.title

	def payPerYear(self):
		# 52 weeks * 5 days a week * 8 hours a day
		pay = 52 * 5 * 8 * self.ratePerHour
		return pay

class Manager(Employee):

	def __init__(self, name, title, salary, reportsList = None):
		self.salary = float(salary)
		if reportsList is None:
			reportsList = []

		self.reportsList = reportsList
		super().__init__(name, title)

	def getReports(self):
		return self.reportsList

	def payPerYear(self, giveBonus = False):
		pay = self.salary
		if giveBonus == True:
			pay = pay + (0.10 * self.salary) #add a bonus of 10%
			print(self.name, 'gets a bonus for good work.')
		return pay


oEmployee1 = Employee("Joe Smith", "Pizza Maker", 16)
oEmployee2 = Employee("Javier Menendez", "Cashier", 16)
oManager = Manager("Alicia Jones", "Pizza Restaurant Manager", 55000, [oEmployee1, oEmployee2])

#Call methods of the Employee objects

print('Employee name:', oEmployee1.getName())
print('Employee salary:', oEmployee1.payPerYear())
print('Employee name:', oEmployee2.getName())
print('Employee salary:', oEmployee2.payPerYear())
print()

#Call methods of the Manager object

print('Manager name:', oManager.getName())
print('Manager salary:', oManager.payPerYear(True))
reportsList = oManager.getReports()
for oEmployee in reportsList:
	print(oEmployee.getName(), oEmployee.getTitle())