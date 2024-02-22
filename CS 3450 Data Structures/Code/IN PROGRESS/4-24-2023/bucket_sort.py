#Bucket sort example using the built-in sorted function

def bucket_sort(array):
	bucket = []

	#Create empty buckets
	for i in range(len(array)):
		bucket.append([])

	# Insert elements into their respective buckets
	for j in array:
		index_b = int(10 * j)
		bucket[index_b].append(j)

	# Sort the elements of each bucket
	for i in range(len(array)):
		bucket[i] = sorted(bucket[i])

	#Get the sorted elements
	k = 0
	for i in range(len(array)):
		for j in range(len(bucket[i])):
			array[k] = bucket[i][j]
			k += 1

	return array

test_array = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.45]
print("Original array is:", test_array)
print("Sorted array using bucket sort is:", bucket_sort(test_array))