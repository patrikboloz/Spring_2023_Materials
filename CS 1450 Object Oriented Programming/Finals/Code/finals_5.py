class Building():

	def __init__(self, name, size = "Medium"):

		self.name = name
		self.hours = [0,0]
		if size == "Medium":
			self.size = "Medium"
		else:
			self.size = size

	def set_open_hours(self, open_time, close_time):
		self.hours[0] = open_time
		self.hours[1] = close_time
		print("The buildings open time has been updated, now the building will open at:", 
			self.hours[0], "and will close at", self.hours[1], "\n")

	def set_name(self, new_name):
		self.name = new_name
		print("The building has been renamed to:", self.name, "\n")

	def get_name(self):
		return self.name

	def get_size(self):
		return self.size

	def get_hours(self):
		return self.hours

class Storage(Building):

	def __init__(self, name, size = "Big"):
		self.name = name
		self.size = size
		self.hours = [0,0]

class Corner_Store(Building):

	def __init__(self, name, size = "Small"):
		self.name = name
		self.size = size
		self.hours = [0,0]



building1 = Building("Walmart")
building2 = Storage("Amazon Storage")
building3 = Corner_Store("Bob's Deli")

building1.set_open_hours(9, 11)
building2.set_open_hours(1, 10)
building3.set_open_hours(8, 3)


buildings_list = [building1, building2, building3]

for building in buildings_list:
	print("The buildings name is:", building.get_name())
	print("The buildings open hours are:", building.get_hours())
	print("The buildings size is:", building.get_size())
	print("==================")



