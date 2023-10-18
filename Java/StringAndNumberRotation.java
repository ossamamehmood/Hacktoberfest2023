import java.util.*;
public class StringAndNumberRotation {
    public static void main(String[] args) {
        String s=new Scanner(System.in).nextLine();
        String[] a= new String[s.length()];
        for(int i=0;i<s.length();i++){
            a[i]= s.substring(1,s.length())+s.charAt(0);
            s=a[i];
            System.out.print(a[i]+" ");
        }
    }
}
