import java.util.Scanner;
public class ParallelogramArea {
    public static void main(String[] args){
        Scanner input=new Scanner(System.in);
        System.out.println("enter the base: ");
        int base=input.nextInt();
        System.out.println("enter the height: ");
        int height=input.nextInt();
        int area=base*height;
        System.out.println("the area of parallelogram: ");
        System.out.println(area);
    }
}
