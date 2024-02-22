#Example of a quicksort algorithm using Python's lists

def quick_sort(arr, left, right):
	if left < right:
	 	partition_pos = partition(arr, left, right)
	 	quick_sort(arr, left, partition_pos - 1)
	 	quick_sort(arr, partition_pos + 1, right)

	return arr


def partition(arr, left, right):
	i = left
	j = right - 1
	pivot = arr[right]

	while i < j:
		while i < right and arr[i] < pivot:
			i += 1
		while j > left and arr[j] >= pivot:
			j -= 1

		if i < j:
			arr[i], arr[j] = arr[j], arr[i]
	if arr[i] > pivot:
		arr[i], arr[right] = arr[right], arr[i]

	return i



arr_test = [4, 8, 12, 3, 5, 0]
print("Original array is:", arr_test)
print("Sorted array using quick sort is:", quick_sort(arr_test, 0, len(arr_test) - 1))