
import java.util.Scanner;
public class Optimized_Array_Reverse {
    public static void Swap(int arr[]){
        int first=0,last=arr.length-1;
        while(first<last){
            int temp=arr[first];
            arr[first]=arr[last];
            arr[last]=temp;

            first++;
            last--;
        }
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter The Size Of The Array: ");
        int size=sc.nextInt();
        int arr[]=new int[size];
        for(int i=0;i<size;i++){
            System.out.print("Enter Arr["+i+"]:- ");
            int x=sc.nextInt();
            arr[i]=x;
        }
        System.out.println("The Array Is:- ");
        for(int i=0;i<size;i++){
            System.out.print(arr[i]+" ");
        }
        System.out.println("\nThe Reversed Array Is:- ");
        Swap(arr);
        for(int i=0;i<size;i++){
            System.out.print(arr[i]+" ");
        }
    }
}
