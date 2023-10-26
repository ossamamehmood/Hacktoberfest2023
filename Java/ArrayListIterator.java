import java.util.ArrayList;
import java.util.Iterator;

public class ArrayListIteration {
    public static void main(String[] args) {
        // Create an ArrayList and add elements
        ArrayList<Integer> arrayList = new ArrayList<>();
        arrayList.add(20);
        arrayList.add(30);
        arrayList.add(40);
        
        System.out.println("iterator Loop:");
        // Iterate using Iterator
        Iterator<Integer> iterator = arrayList.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }
        
        System.out.println("Advanced For Loop:");
        // Iterate using Advanced For Loop
        for (int num : arrayList) {
            System.out.println(num);
        }
        
        System.out.println("For Loop:");
        // Iterate using regular for loop
        for (int i = 0; i < arrayList.size(); i++) {
            System.out.println(arrayList.get(i));
        }
    }
}
