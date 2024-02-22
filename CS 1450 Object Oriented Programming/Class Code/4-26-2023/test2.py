#Data structures in Python

#Lists - mutable structure
a_list = [1, 2, 3, 4, 5, 6, 7]
b_list = ["patrik", "jaydan", "jeff"]
c_list = [1.5, "Hello World", 90]
d_list = [[1,2,3],[4,5,6]]

#print(a_list)
#print(b_list)
#print(c_list)
#print(d_list)
#print(a_list[0])
#print(b_list[0])
#print(d_list[0][1])
a_list.append(50)

a_list[0] = 100
#print(a_list)

#Tuple - immutable structure
a_tuple = (1, 2, 3, 4, 5, 6, 7)
#print(a_tuple)
#print(a_tuple[0])
#a_tuple[0] = 50

#Dictionary 
a_dictionary = {80: "Patrik", 40:"Aidan", 96:"Jeff"}
#print(a_dictionary[80])

#Sets
a_set = {10, 20, 30, 40, 50, 60, 50, 20, 10}
print(a_set)