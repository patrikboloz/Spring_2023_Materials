#Example of a merge sort algorithm with the use of Python lists

def merge_sort(arr):

	if len(arr) > 1:
		left_arr = arr[:len(arr)//2] #start from zero until the middle index
		right_arr = arr[len(arr)//2:] #start from middle point until the end index

		#Recursion
		merge_sort(left_arr)
		merge_sort(right_arr)

		#Recursion steps

		i = 0 #left arr index
		j = 0 #right att index
		k = 0 #merged arr index

		while i < len(left_arr) and j < len(right_arr):
			if left_arr[i] < right_arr[j]:	
				arr[k] = left_arr[i]
				i += 1
			else:
				arr[k] = right_arr[j]
				j += 1
			k += 1

		while i < len(left_arr):
			arr[k] = left_arr[i]
			i += 1
			k += 1

		while j < len(right_arr):
			arr[k] = right_arr[j]
			j += 1
			k += 1

		return arr

arr_test = [4, 8, 12, 3, 5, 0]
print("Original array is:", arr_test)
print("Sorted array using merge sort is:", merge_sort(arr_test))