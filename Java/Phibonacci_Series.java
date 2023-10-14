// To Print phibonacci Series using iterative method 
import java.util.Scanner;
public class Phibonacci__Series {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int a=0;
		int b=1;
		int c=0;
		int n=sc.nextInt();
		for(int i=0;i<n;i++) {
			System.out.print(a+" ");
			c=a+b;
			a=b;
			b=c;
			
		}
}}
