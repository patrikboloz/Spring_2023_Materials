a_list = [1,2,3,4,5]
print("Your list is:", a_list)
new_list = []

for number in a_list:
	number -= 1
	squared_number = a_list[number] * a_list[number]
	#print(a_list[number])
	new_list.append(squared_number)
	
print("Your new list of squared numbers is:", new_list)


