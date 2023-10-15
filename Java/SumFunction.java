import java.util.Scanner;

public class SumFunction {
    public static void main(String[] args) {
        sum();

    }

    static void sum() {

        Scanner in = new Scanner(System.in);
        System.out.println("Gimme The First Number:");
        int a = in.nextInt();
        System.out.println("Gimme The Second Number");
        int b = in.nextInt();
        int sum = a + b;
        System.out.println("The Sum of the numbers you gave is " + sum );
}
}
