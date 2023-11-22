import java.util.Arrays;

public class QuickSort {
    public static void main(String[] args) {
        int[] arr = {4,2,6,7,5,1};
        sort(arr,0, arr.length - 1);
        System.out.println(Arrays.toString(arr));
    }

    static void sort (int[] nums,int low,int hi){
        if(low>=hi){
            System.out.println("Done");
            return;
        }
        int s = low;
        int e = hi;
        int m = s + (e - s) / 2;
        int pivot = nums[m];

        while (s <= e){
            while(nums[s] < pivot){
                s++;
            }
            while(nums[e] > pivot){
                e--;
            }

            if(s<=e){
                int temp = nums[s];
                nums[s] = nums[e];
                nums[e] = temp;
                s++;
                e--;
            }
        }

        sort(nums,low,e);

        sort(nums,s,hi);

    }
}