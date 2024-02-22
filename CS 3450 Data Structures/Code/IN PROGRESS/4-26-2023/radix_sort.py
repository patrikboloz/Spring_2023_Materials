# Radix sort inm Python

#Using counting sort to sort elements in the basis of significant places

def counting_sort(array, place):
	size = len(array)
	output = [0] * size
	count = [0] * 10

	#Calculate count of elements
	for i in range(0, size):
		index = array[i] // place
		count[index % 10] += 1

	#Calculate the cumulative count
	for i in range(1,10):
		count[i] += count[i - 1]

	#Place the elements in sorted order
	i = size - 1
	while i >= 0:
		index = array[i] // place
		output[count[index % 10] - 1] = array[i]
		count[index % 10] -= 1
		i -= 1

	for i in range(0, size):
		array[i] = output[i]

def radix_sort(array):
	#Get the maximum element
	max_element = max(array)

	#Apply counting sort to sort elements based on place value
	place = 1
	while max_element // place > 0:
		counting_sort(array, place)
		place *= 10

	return array


data = [121, 432, 564, 23, 1, 45, 788]
print("Original array:", data)
print("Sorted array using radix sort:", radix_sort(data))