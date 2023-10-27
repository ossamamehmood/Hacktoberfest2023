\\Java program to write a merge sort
package mergesort;

import java.util.Random;
import java.util.Scanner;

/* Class MergeSort */
public class MergeSort 
{
/* Merge Sort function */
	public static void sort(int[] a, int low, int high) 
	{
		int N = high - low;         
		if (N <= 1) 
			return; 
		int mid = low+N/2; 
		// recursively sort 
		sort(a, low, mid); 
		sort(a, mid, high); 
		// merge two sorted subarrays
		int[] temp = new int[N];
		int i = low, j = mid;
		for (int k = 0; k < N; k++) 
		{
		if (i == mid)  
			temp[k] = a[j++];
		else if (j == high) 
			temp[k] = a[i++];
		else if (a[j]<a[i]) 
			temp[k] = a[j++];
		else 
			temp[k] = a[i++];
		}    
		for (int k = 0; k < N; k++) 
		a[low + k] = temp[k];         
	}
	/* Main method */
	public static void main(String[] args) 
	{
		Scanner scanner = new Scanner( System.in );        
		System.out.println("Merge Sort Test\n");
		System.out.print("Enter the size of the array: ");
		int size = scanner.nextInt();
		int[] array = new int[size];
		Random random = new Random();
		System.out.println("Populating array with random numbers...");
		for (int i = 0; i < size; i++) {
		array[i] = random.nextInt();
		}
		System.out.println("Original array:");
		for (int i = 0; i < size; i++) {
		System.out.println(array[i] + " ");
		}
		long startTime = System.currentTimeMillis();
		
		sort(array, 0, size);
		long endTime = System.currentTimeMillis();
		long executionTime = endTime - startTime;
		/** Print sorted Array **/
		System.out.println("\nElements after sorting ");
		for (int i = 0; i < size; i++) {
		System.out.println(array[i] + " ");
		}
		System.out.println("Total Time taken to sort the numbers is: "+executionTime+" MilliSeconds");
		scanner.close();
	}    
}
