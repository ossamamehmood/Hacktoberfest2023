package com.company;

import java.util.Arrays;

public class CyclicSort1 {
    public static void main(String[] args) {
        int[] arr = {4,1,5,2,3};
        sort(arr);
        System.out.println(Arrays.toString(arr));
    }
    static void sort(int[] arr){
        int i =0;
        while (i< arr.length){
            int correct = arr[i]-1;
            if (arr[i]!= arr[correct]){
                int temp = arr[i];
                arr[i]= arr[correct];
                arr[correct] = temp;
// this cyclic sort is mostly used for continous nos like 1 to n
            }
            else
                i++;

        }
    }
}
