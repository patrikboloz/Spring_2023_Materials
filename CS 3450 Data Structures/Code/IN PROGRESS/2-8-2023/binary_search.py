#Binary search implementation in Python by using recursion

def binary_search(data, target, low, high):
	"""Return True if target is found in indicated portion of a Python list

	The search only considers the portion from data[low] to data[high] inclusive.
	"""

	if low > high:
		return False  #interval is empty, no match
	else:
		mid = (low + high) // 2
		if target == data[mid]:
			return True #we found our match, we are done
		elif target < data[mid]:
			# recursion on the portion left of the middle
			return binary_search(data, target, low, mid - 1)
		else:
			# recursion on the portion right of the middle
			return binary_search(data, target, mid + 1, high)

testing_list = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]

unsorted_list = [5,4,8,2,1,0,3,6,7,58,45]

target = 58 
low = 0
high = len(testing_list) - 1

print(binary_search(testing_list, target, low, high))