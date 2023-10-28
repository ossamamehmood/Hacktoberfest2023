#include <iostream>

// Merge two subarrays into one sorted array.
void merge(int arr[], int start, int mid, int end) {
    int leftSize = mid - start + 1;
    int rightSize = end - mid;

    int* leftArray = new int[leftSize];
    int* rightArray = new int[rightSize];


    // Copy elements to the left and right subarrays.
    for (int i = 0; i < leftSize; i++) {
        leftArray[i] = arr[start + i];
    }
    for (int i = 0; i < rightSize; i++) {
        rightArray[i] = arr[mid + 1 + i];
    }

    int leftIndex = 0;
    int rightIndex = 0;
    int mergedIndex = start;

    // Merge the left and right subarrays back into the original array.
    while (leftIndex < leftSize && rightIndex < rightSize) {
        if (leftArray[leftIndex] <= rightArray[rightIndex]) {
            arr[mergedIndex++] = leftArray[leftIndex++];
        } else {
            arr[mergedIndex++] = rightArray[rightIndex++];
        }
    }

    // Copy any remaining elements from the left and right subarrays.
    while (leftIndex < leftSize) {
        arr[mergedIndex++] = leftArray[leftIndex++];
    }
    while (rightIndex < rightSize) {
        arr[mergedIndex++] = rightArray[rightIndex++];
    }

    delete[] leftArray;
    delete[] rightArray;
}

// Recursively sort an array using merge sort.
void mergeSort(int arr[], int start, int end) {
    if (start < end) {
        int mid = start + (end - start) / 2;

        // Sort the left and right halves of the array.
        mergeSort(arr, start, mid);
        mergeSort(arr, mid + 1, end);

        // Merge the sorted halves.
        merge(arr, start, mid, end);
    }
}

//main function
int main() {
    int arr[] = {2, 10, 68, 3, 1};
    int arraySize = sizeof(arr) / sizeof(arr[0]);

    // Sort the array using merge sort.
    mergeSort(arr, 0, arraySize - 1);

    // Display the sorted array.
    for (int i = 0; i < arraySize; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
