public class BinarySearch {
    public static void main(String[] args) {
        int[] arr = {-18, -12, -4, 0, 1, 2, 3, 4, 9, 12, 56};
        int target = 0;
        int ans = binarySearch(arr, target);
        if(ans != -1){
            System.out.println("Element found at the index: " + (ans + 1));
        } else {
            System.out.println("Element not found in the Array.");
        }
    }



    static int binarySearch(int[] arr, int target){
        int start = 0;
        int end = arr.length - 1;

        while (start <= end){
            // find the middle element
//            int mid = (start + mid)/2; // might be possible that (start + end ) will exceed the limit of a int in java then will give error
            int mid = start + (end - start)/2;

            if (target < arr[mid]){
                end = mid -1;
            }
            else if (target > arr[mid]){
                start = mid + 1;

            }
            else {
                // ans found
                // return the index
                return mid;
            }

        }
        // return -1 if it does not exist
        return -1;
    }
}
