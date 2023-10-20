public class ArraySecondHighestNumber {

    public static void main(String[] args) {
        int[] arr = {1000, 100, 3, 40, 4000};

        int highest = Integer.MIN_VALUE;
        int secondHighest = Integer.MIN_VALUE;
        for (int j : arr) {
            if (j > highest) {
                secondHighest = highest;
                highest = j;
            } else {
                secondHighest = j;
            }
        }
        System.out.println(secondHighest);
    }
}
