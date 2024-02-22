class Hotel():

	def __init__(self, hotel_name):
		self.hotel_name = hotel_name
		self.hotel_guests_list = []

	def add_guest(self, guest_name):
		self.hotel_guests_list.append(guest_name)
		print(guest_name, "was checked in. Welcome!")

	def check_out_guest(self, guest_name):
		self.hotel_guests_list.remove(guest_name)
		print(guest_name, "was checked out. Good bye!")

	def get_list(self):
		return self.hotel_guests_list

hotel1 = Hotel("Hilton")
hotel1.add_guest("Patrik")
hotel1.add_guest("Phillip")
hotel1.add_guest("Erick")
print("Current guest list:", hotel1.get_list())
hotel1.check_out_guest("Erick")