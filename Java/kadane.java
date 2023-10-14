import java.util.*;
public class kadane {
    public static void kad(int arr[]){
        int current_sum = 0;
        int max_sum = Integer.MIN_VALUE;

        for(int i = 0; i < arr.length; i++){
            current_sum += arr[i];
            if(current_sum < 0){
                current_sum = 0;
            }
            max_sum = Math.max(max_sum, current_sum);
        }
        System.out.println("max sum: " + max_sum);
    }
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int input[] = new int[6];

        for(int i = 0; i < input.length; i++){
            input[i] = sc.nextInt();
        }

        kad(input);
    }
}
