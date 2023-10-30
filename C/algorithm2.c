//Add different Searching and sorting using C with algorithm

//C Code for Binary Search

#include <stdio.h>

int binarySearch(int arr[], int left, int right, int key) {
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == key)
            return mid;
        
        if (arr[mid] < key)
            left = mid + 1;
        else
            right = mid - 1;
    }
    
    return -1; // Key not found
}

int main() {
    int arr[] = {2, 3, 4, 10, 40};
    int n = sizeof(arr) / sizeof(arr[0]);
    int key = 10;
    
    int result = binarySearch(arr, 0, n - 1, key);
    
    if (result != -1)
        printf("Element found at index %d\n", result);
    else
        printf("Element not found\n");
    
    return 0;
}
