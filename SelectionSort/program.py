def selectionSort(array):
	# Write your code here.
	for i in range(len(array)-1):
		for j in range(i+1, len(array)):
			if array[j] < array[i]:
				array[i], array[j] = array[j], array[i]
	return array
