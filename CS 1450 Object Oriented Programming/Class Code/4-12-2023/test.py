
def average_list(a_list):


	list_sum = sum(a_list)
	list_len = len(a_list)
	average = list_sum/list_len
	return average



num_list = [1,2,3,4,5,6,7,8,9,10]
print(average_list(num_list))