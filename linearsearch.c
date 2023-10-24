
#include <stdio.h>

// linear search function that searches the key in arr
int linearSearch(int* arr, int size, int key)
{
	// starting traversal
	for (int i = 0; i < size; i++) {
		// checking condition
		if (arr[i] == key) {
			return i;
		}
	}
	return -1;
}

// Driver code
int main()
{
	int arr[10] = { 3, 4, 1, 7, 5, 8, 11, 42, 3, 13 };
	int size = sizeof(arr) / sizeof(arr[0]);
	int key = 4;

	// calling linearSearch
	int index = linearSearch(arr, size, key);

	// printing result based on value returned by
	// linearSearch()
	if (index == -1) {
		printf("The element is not present in the arr.");
	}
	else {
		printf("The element is present at arr[%d].", index);
	}

	return 0;
}
