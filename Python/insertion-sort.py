# Python program for implementation of Iterative insertion sort

def insertionSort(arr):

	# Traverse through the array
	for i in range(1, len(arr)):

		key = arr[i]
    
    # Move elements that are greater than the key to one
    # position right.
		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key


# Driver code
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
for i in range(len(arr)):
	print ("% d" % arr[i])
