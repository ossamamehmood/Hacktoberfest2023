#ifndef SORTING_ALL_H
#define SORTING_ALL_H

#include <vector>
#include <iostream>

namespace SortingAlgorithms
{
    class Sorting
    {
    public:
        Sorting() {}

        void selectionSort(std::vector<int> &arr)
        {
            for (int i = 0; i < arr.size() - 1; i++)
            {
                for (int j = i + 1; j < arr.size(); j++)
                {
                    if (arr[i] > arr[j])
                    {
                        std::swap(arr[i], arr[j]);
                    }
                }
                // Debugging
                #ifdef DEBUG
                printArray(arr);
                #endif
            }
        }

        void bubbleSort(std::vector<int> &arr)
        {
            for (int i = 0; i < arr.size() - 1; i++)
            {
                for (int j = 0; j < arr.size() - i - 1; j++)
                {
                    if (arr[j] > arr[j + 1])
                    {
                        std::swap(arr[j], arr[j + 1]);
                    }
                }
                // Debugging
                #ifdef DEBUG
                printArray(arr);
                #endif
            }
        }

        void insertionSort(std::vector<int> &arr)
        {
            for (int i = 1; i < arr.size(); i++)
            {
                int j = i - 1;
                int current = arr[i];

                while (j >= 0 && arr[j] > current)
                {
                    arr[j + 1] = arr[j];
                    j--;
                }
                arr[j + 1] = current;
                // Debugging
                #ifdef DEBUG
                printArray(arr);
                #endif
            }
        }

        void mergeSort(std::vector<int> &arr)
        {
            mergeSortRecursive(arr, 0, arr.size() - 1);
        }

        void quickSort(std::vector<int> &arr)
        {
            quickSortRecursive(arr, 0, arr.size() - 1);
        }

        void heapSort(std::vector<int> &arr)
        {
            buildMaxHeap(arr);
            for (int i = arr.size() - 1; i > 0; i--)
            {
                std::swap(arr[0], arr[i]);
                maxHeapify(arr, 0, i);
            }
        }

        void hybridSort(std::vector<int> &arr)
        {
            hybridSortRecursive(arr, 0, arr.size() - 1);
        }

        void printSortedArray(const std::vector<int> &arr)
        {
            std::cout << "Sorted Array: { ";
            for (int num : arr)
            {
                std::cout << num << ", ";
            }
            std::cout << " }" << std::endl;
        }

    private:
        const int INSERTION_THRESHOLD = 16;

        void mergeSortRecursive(std::vector<int> &arr, int left, int right)
        {
            if (left < right)
            {
                int mid = left + (right - left) / 2;
                mergeSortRecursive(arr, left, mid);
                mergeSortRecursive(arr, mid + 1, right);
                merge(arr, left, mid, right);
                // Debugging
                #ifdef DEBUG
                printArray(arr);
                #endif
            }
        }

        void quickSortRecursive(std::vector<int> &arr, int low, int high)
        {
            if (low < high)
            {
                int pivotIndex = partition(arr, low, high);
                quickSortRecursive(arr, low, pivotIndex - 1);
                quickSortRecursive(arr, pivotIndex + 1, high);
                // Debugging
                #ifdef DEBUG
                printArray(arr);
                #endif
            }
        }

        void buildMaxHeap(std::vector<int> &arr)
        {
            for (int i = arr.size() / 2 - 1; i >= 0; i--)
            {
                maxHeapify(arr, i, arr.size());
            }
        }

        void maxHeapify(std::vector<int> &arr, int root, int size)
        {
            int largest = root;
            int left = 2 * root + 1;
            int right = 2 * root + 2;

            if (left < size && arr[left] > arr[largest])
            {
                largest = left;
            }

            if (right < size && arr[right] > arr[largest])
            {
                largest = right;
            }

            if (largest != root)
            {
                std::swap(arr[root], arr[largest]);
                maxHeapify(arr, largest, size);
            }
        }

        void hybridSortRecursive(std::vector<int> &arr, int left, int right)
        {
            if (left < right)
            {
                if (right - left + 1 < INSERTION_THRESHOLD)
                {
                    insertionSort(arr, left, right);
                }
                else
                {
                    int pivotIndex = partition(arr, left, right);
                    hybridSortRecursive(arr, left, pivotIndex - 1);
                    hybridSortRecursive(arr, pivotIndex + 1, right);
                }
                // Debugging
                #ifdef DEBUG
                printArray(arr);
                #endif
            }
        }

        int partition(std::vector<int> &arr, int low, int high)
        {
            int pivot = arr[high];
            int i = low - 1;
            for (int j = low; j < high; j++)
            {
                if (arr[j] <= pivot)
                {
                    i++;
                    std::swap(arr[i], arr[j]);
                }
            }
            std::swap(arr[i + 1], arr[high]);
            return i + 1;
        }

        void printArray(const std::vector<int> &arr)
        {
            std::cout << "Array: { ";
            for (int num : arr)
            {
                std::cout << num << ", ";
            }
            std::cout << " }" << std::endl;
        }
    };
} // namespace SortingAlgorithms

#endif
