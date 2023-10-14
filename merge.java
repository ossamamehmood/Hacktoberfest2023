public class MergeSort {

    public static void mergeSort(int[] arr) {
        if (arr.length <= 1) {
            return;
        }

        int mid = arr.length / 2;
        int[] left = new int[mid];
        int[] right = new int[arr.length - mid];

        // Split the array into left and right halves
        System.arraycopy(arr, 0, left, 0, mid);
        System.arraycopy(arr, mid, right, 0, arr.length - mid);

        // Recursive calls to sort the left and right halves
        mergeSort(left);
        mergeSort(right);

        // Merge the sorted halves
        merge(arr, left, right);
    }

    public static void merge(int[] arr, int[] left, int[] right) {
        int leftIndex = 0;
        int rightIndex = 0;
        int mergedIndex = 0;

        // Compare elements from left and right arrays and merge them in sorted order
        while (leftIndex < left.length && rightIndex < right.length) {
            if (left[leftIndex] <= right[rightIndex]) {
                arr[mergedIndex] = left[leftIndex];
                leftIndex++;
            } else {
                arr[mergedIndex] = right[rightIndex];
                rightIndex++;
            }
            mergedIndex++;
        }

        // Merge the remaining elements from left array
        while (leftIndex < left.length) {
            arr[mergedIndex] = left[leftIndex];
            leftIndex++;
            mergedIndex++;
        }

        // Merge the remaining elements from right array
        while (rightIndex < right.length) {
            arr[mergedIndex] = right[rightIndex];
            rightIndex++;
            mergedIndex++;
        }
    }
