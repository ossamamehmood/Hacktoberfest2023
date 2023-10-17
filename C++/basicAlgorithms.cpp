#include <iostream>
#include <ctime>
using namespace std;

// Sorting algorithms
void insertionOrder(int arr[], int n);
void bubbleOrder(int arr[], int n);
void swap(int &x, int &y); // for the bubbleOrder
void merge(int arr[], int begin, int middle, int end);
void mergeOrder(int arr[], int left, int right);
// Searching algorithms
int sequentialSearch(int arr[], int n, int x);
int binarySearch_Iterative(int arr[], int n, int x);
int binarySearch_Recursive(int arr[], int low, int high, int x);

void printArray(int arr[], int n); // to print array

int main()
{
    int size = 10;  // size of the arrays
    srand(time(0)); // creates a new seed for rand()

    // INSERTION ORDER
    cout << "\nINSERTION ORDER" << endl;
    cout << "The unsorted array is: ";
    int array1[size];
    for (int i = 0; i < size; i++)
    {
        array1[i] = rand() % 100;
        cout << array1[i] << " ";
    }
    insertionOrder(array1, size);
    printArray(array1, size);

    // BUBBLE ORDER
    cout << "\nBUBBLE ORDER" << endl;
    cout << "The unsorted array is: ";
    int array2[size];
    for (int i = 0; i < size; i++)
    {
        array2[i] = rand() % 100;
        cout << array2[i] << " ";
    }
    bubbleOrder(array2, size);
    printArray(array2, size);

    // MERGE ORDER
    cout << "\nMERGE ORDER" << endl;
    cout << "The unsorted array is: ";
    int array3[size];
    for (int i = 0; i < size; i++)
    {
        array3[i] = rand() % 100;
        cout << array3[i] << " ";
    }
    mergeOrder(array3, 0, size - 1);
    printArray(array3, size);

    // SEQUENTIAL SEARCH
    cout << "\nSEQUENTIAL SEARCH" << endl;
    cout << "The sorted array is: ";
    int array4[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int n = sizeof(array4) / sizeof(array4[0]);
    for (int i = 0; i < n; i++)
        cout << array4[i] << " ";
    int x;
    cout << "\nEnter a number: ";
    cin >> x; // element to be found
    cout << "Element is in index: " << sequentialSearch(array4, n, x) << endl;

    // BINARY SEARCH ITERATIVE AND RECURSIVE
    cout << "\nBINARY SEARCH" << endl;
    cout << "The sorted array is: ";
    int array[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    n = sizeof(array) / sizeof(array[0]);
    for (int i = 0; i < n; i++)
        cout << array[i] << " ";
    int x2;
    cout << "\nEnter a number: ";
    cin >> x2; // element to be found
    cout << "Element is in index: " << binarySearch_Iterative(array, n - 1, x2) << " (using iterative method)" << endl;
    cout << "Element is in index: " << binarySearch_Recursive(array, 0, n - 1, x2) << " (using recursive method)\n"
         << endl;

    return 0;
}

void insertionOrder(int arr[], int n)
{
    for (int i = 1; i < n; i++)
    {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
    // Complexity: O(n^2)
}
void bubbleOrder(int arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n - i; j++)
        {
            if (arr[j] > arr[j + 1])
                swap(arr[j], arr[j + 1]);
        }
    }
    // Complexity: O(n^2)
}
void swap(int &x, int &y)
{
    int temp = x;
    x = y;
    y = temp;
    // Complexity: O(1)
}
void merge(int arr[], int begin, int middle, int end)
{
    int n1 = middle - begin + 1;
    int n2 = end - middle;
    int l[n1], r[n2]; // declare new sub-arrays
    for (int i = 0; i < n1; i++)
        l[i] = arr[begin + i];
    for (int j = 0; j < n2; j++)
        r[j] = arr[middle + 1 + j];
    int i = 0;
    int j = 0;
    int k = begin;
    while (i < n1 && j < n2)
    {
        if (l[i] <= r[j])
        {
            arr[k] = l[i];
            i++;
        }
        else
        {
            arr[k] = r[j];
            j++;
        }
        k++;
    }
    while (i < n1)
    {
        arr[k] = l[i];
        i++;
        k++;
    }
    while (j < n2)
    { // i????????
        arr[k] = r[j];
        j++;
        k++;
    }
    // Complexity: O(nlog n)
}
void mergeOrder(int arr[], int left, int right)
{
    if (left < right)
    {
        int mid = left + (right - left) / 2;
        mergeOrder(arr, left, mid);
        mergeOrder(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
    // See complexity on merge()
}
int sequentialSearch(int arr[], int n, int x)
{
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == x)
            return i;
    }
    return -1;
    // Complexity: O(n)
}
int binarySearch_Iterative(int arr[], int n, int x)
{
    int low = 0;
    int high = n;
    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (x == arr[mid])
            return mid;
        else if (x > arr[mid])
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;
    // Complexity: O(log n)
}
int binarySearch_Recursive(int arr[], int low, int high, int x)
{
    if (low <= high)
    {
        int mid = (low + high) / 2;
        if (x == arr[mid])
            return mid;
        else if (x > arr[mid])
            return binarySearch_Recursive(arr, mid + 1, high, x);
        else
            return binarySearch_Recursive(arr, low, mid - 1, x);
    }
    return -1;
    // Complexity: O(log n)
}
void printArray(int arr[], int n)
{
    cout << "\nAfter the method the array is: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
    // Complexity: O(n)
}