import java.util.*;
public class MergeSort {
    public static void mergeSort(int[] arr) {
        if (arr == null || arr.length <= 1) {
            return; 
        // Base case: if the array is empty or has only one element, it's already sorted
        }

        // Find the middle index of the array
        int middle = arr.length / 2;

        // Split the array into two halves
        int[] left = new int[middle];
        int[] right = new int[arr.length - middle];
        System.arraycopy(arr, 0, left, 0, middle);
        System.arraycopy(arr, middle, right, 0, arr.length - middle);

        // Recursively sort the two halves
        mergeSort(left);
        mergeSort(right);

        // Merge the sorted halves
        merge(arr, left, right);
    }

    public static void merge(int[] result, int[] left, int[] right) {
        int i = 0; // Index for the left array
        int j = 0; // Index for the right array
        int k = 0; // Index for the merged array

        // Compare elements from left and right arrays and merge them in sorted order
        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                result[k] = left[i];
                i++;
            } else {
                result[k] = right[j];
                j++;
            }
            k++;
        }

        // Copy the remaining elements of left and right arrays (if any)
        while (i < left.length) {
            result[k] = left[i];
            i++;
            k++;
        }

        while (j < right.length) {
            result[k] = right[j];
            j++;
            k++;
        }
    }

    public static void main(String[] args) {
        Scanner kvp=new Scanner(System.in);
        int n;
        System.out.println("Enter length of array:");
        n=kvp.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter elements of array:");
        for(int i=0;i<n;i++)
        {
            arr[i]=kvp.nextInt();
            
        }
        // Print the original array
        System.out.println("Original array:");
        printArray(arr);
        
        // Call the mergeSort function and pass original array arr as paramater
        mergeSort(arr);
        System.out.println("\nSorted array:");
        printArray(arr);
    }
// Function to print an array
    public static void printArray(int[] arr) {
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}
