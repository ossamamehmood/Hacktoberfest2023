#include <stdio.h>
#include <stdlib.h>

void merge(int arr[], int left[], int leftSize, int right[], int rightSize) {
    int i = 0, j = 0, k = 0;

    // Compare elements from left and right arrays and merge them in sorted order
    while (i < leftSize && j < rightSize) {
        if (left[i] <= right[j]) {
            arr[k] = left[i];
            i++;
        } else {
            arr[k] = right[j];
            j++;
        }
        k++;
    }

    // Copy the remaining elements of left and right arrays (if any)
    while (i < leftSize) {
        arr[k] = left[i];
        i++;
        k++;
    }

    while (j < rightSize) {
        arr[k] = right[j];
        j++;
        k++;
    }
}

void mergeSort(int arr[], int size) {
    if (size <= 1) {
        return; // Base case: if the array has only one element or is empty, it's already sorted
    }

    // Find the middle index of the array
    int middle = size / 2;

    // Split the array into two halves
    int *left = (int *)malloc(middle * sizeof(int));
    int *right = (int *)malloc((size - middle) * sizeof(int));

    // Copy data to temporary arrays left[] and right[]
    for (int i = 0; i < middle; i++) {
        left[i] = arr[i];
    }

    for (int i = middle; i < size; i++) {
        right[i - middle] = arr[i];
    }

    // Recursively sort the two halves
    mergeSort(left, middle);
    mergeSort(right, size - middle);

    // Merge the sorted halves
    merge(arr, left, middle, right, size - middle);

    // Free the allocated memory for temporary arrays
    free(left);
    free(right);
}
// Function to print an array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    printf("Enter length of array: ");
    int n;
    scanf("%d",&n);
    int arr[n];
    printf("Enter length of array: ");
    for(int i=0;i<n;i++)
    {
        scanf("%d ",&arr[i]);
    }
    printf("Original array: ");
    printArray(arr, size);

    mergeSort(arr, size);
    
    printf("Sorted array: ");
    printArray(arr, size);

    return 0;
}
