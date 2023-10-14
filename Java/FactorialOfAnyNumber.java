// Program to find factorial of any number using Iterative method

import java.util.Scanner;

public class FactorialOfAnyNumber {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the Number whose Factorial has to be calculated ");
		int n = sc.nextInt();
		int fact=1;
		for(int i=n;i>=1; i--)
		{
			fact*=i;
		}
        System.out.println("The factorial is  "+ fact);
       
	}

}
