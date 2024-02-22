
a_list = [2, 4, 8, 10, 15]
#print(a_list)

for i in a_list:
	i = i + 1
	#print(i)

j = 0
while j < len(a_list):
	a_list[j] = a_list[j] + 1
	#print(a_list)
	j = j + 1 


a = 10
while a < 20:
	#print("Hello World")
	a = a + 1

print(a) #a is 20
	
while a < 100:

	if a == 15:
		print("A is equal to 15")
		break

	elif a == 20:
		print("A is equal to 20.")
		a = 15
	else:
		print("A is not equal to any number we're looking for.")

print(a)
