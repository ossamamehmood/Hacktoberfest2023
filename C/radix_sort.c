#include <stdio.h>
#include <stdlib.h>


int findMax(int arr[], int n) {
    int max = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}


void countingSort(int arr[], int n, int place) {
    const int max = 10; 
    int output[n];
    int count[max];

    for (int i = 0; i < max; i++) {
        count[i] = 0;
    }

    
    for (int i = 0; i < n; i++) {
        count[(arr[i] / place) % 10]++;
    }

    
    for (int i = 1; i < max; i++) {
        count[i] += count[i - 1];
    }

    
    for (int i = n - 1; i >= 0; i--) {
        output[count[(arr[i] / place) % 10] - 1] = arr[i];
        count[(arr[i] / place) % 10]--;
    }

    
    for (int i = 0; i < n; i++) {
        arr[i] = output[i];
    }
}


void radixSort(int arr[], int n) {
    int max = findMax(arr, n);

    
    for (int place = 1; max / place > 0; place *= 10) {
        countingSort(arr, n, place);
    }
}

int main() {
    int n;
    printf("Enter the number of elements: ");
    scanf("%d", &n);

    int arr[n];
    printf("Enter the elements: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    radixSort(arr, n);

    printf("Sorted array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
