import java.util.Scanner;

public class Occurrence {

    public static void main(String[] args) {

        int size;
        System.out.println("Enter the size of array");
        Scanner input = new Scanner(System.in);
        size = input.nextInt();
        int[] arr = new int[size];

        System.out.println("Enter the elements of an array");

        //taking input array from users

        for (int i = 0; i < size; i++) {
            arr[i] = input.nextInt();
        }

        // sorting the array

        for (int i = 0; i < size; i++) {

            for (int j = i + 1; j < size; j++) {

                // swap the elements if 1st element is larger than other elements
                if (arr[i] > arr[j]) {
                    int temp;
                    temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }

        //checking occurrence

        for (int i = 0; i < size; i++) {

            int count = 1;

            for (int j = i + 1; j < size; j++) {

                if (arr[i] == arr[j]) {
                    count++;
                } else {
                    break;
                }

            }

            System.out.println("The occurrence of " + arr[i] + " is " + count);
            i = i + count - 1;

        }

    }


}