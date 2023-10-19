public class square {
	static void squarefx(int x) {
		x=x*x;
		System.out.println("The square of the given number is "+x);
	}

	public static void main(String[] args) {
     System.out.println("Program to find the square of the given number:)");
     java.util.Scanner sc=new java.util.Scanner(System.in);
     int x;
     String choice;
     do {
    	 System.out.println("Enter the number");
    	  x=sc.nextInt();
    	 squarefx( x);
    	 System.out.println("Do You Stll Want To Continue [YES/No]");
    	 choice=sc.next();
     }
     while(choice.equalsIgnoreCase("yes"));
     sc.close();
	}

}
