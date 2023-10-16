public class DivideAndConquer1 {
    public static int findMax(int[] arr) {
        return findMax(arr, 0, arr.length - 1);
    }

    private static int findMax(int[] arr, int left, int right) {
        if (left == right) {
            return arr[left];
        }

        int mid = (left + right) / 2;

        int maxLeft = findMax(arr, left, mid);
        int maxRight = findMax(arr, mid + 1, right);

        return Math.max(maxLeft, maxRight);
    }

    public static void main(String[] args) {
        int[] arr = {3, 9, 7, 2, 8, 6};
        int max = findMax(arr);
        System.out.println("The maximum element in the array is: " + max);
    }
}
