package com.leet_solns;

public class binary_search {
    public static int binarySearch(int [] arr, int target){
        int start = 0;
        int end = arr.length - 1;
        while (start <= end){
            //int mid = (start + end)/2; //it may give some error because start + end may exceed the linit of the int
            int mid = start + (end - start)/2;

            if (target > arr[mid]){
                start = mid + 1;
            }
            else if(target < arr[mid]){
                end = mid - 1;
            }
            else {
                return mid;
            }
        }
        return -1;
    }
    public static void main(String[] args) {
         int [] arr = {2 , 3, 4 ,16 ,22,25,26};
         int ans = binarySearch(arr,23);
        System.out.println(ans);
    }
}
