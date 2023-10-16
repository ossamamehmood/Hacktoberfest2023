import java.util.ArrayList;

public class StackImplementation {
    static class stackArrList{
        static ArrayList<Integer> list = new ArrayList<>(); 
        
        public static boolean IsEmpty(){
            return list.size()== 0;
        }

        public static void  pushA(int data){
        list.add(data);
    }

        public static int popA(){
            if(IsEmpty()){
                return -1;
            }
            int top = list.get(list.size()-1);
            list.remove(list.size()-1);
            return top;
        }

        public static int peekA(){
            if(IsEmpty()){
                return -1;
            }
            return list.get(list.size()-1);
        }

    }

    static class Node{
        int data;
        Node next;

        Node(int data){
            
            this.data = data;
            next = null;
        }
    }

    static class stackLinkedlist{
        public static Node head;

        public static void pushL(int data){
            Node newnode = new Node(data);
            if(head==null){
                head = newnode ;
                return ;
            }
            newnode.next = head;
            head = newnode;

        }
        
        public static boolean isempty(){
            return head==null;
        }

        public static int popL(){
            if(head==null){
                return -1;
            }
            int top = head.data;
            head = head.next;
            return top;
        }

        public static int peekL(){
            if(head==null){
                return -1;
            }
            return head.data;
        } 

    }

    public static void main(String[] args) {
        stackArrList s = new stackArrList();
        stackLinkedlist s1 = new stackLinkedlist(); 
        
        // s.pushA(1);
        // s.pushA(2);
        // s.pushA(3);
        // s.pushA(4);
        // s.pushA(5);
        // s.pushA(6);
        // s.popA();
        // s.popA();
        
        /* Calling a function in static way (it doesnot show any warning)
         But it is inconvenient to call method without creating list
         */
        // stackArrList.pushA(5);
        // stackArrList.pushA(4);
        // stackArrList.pushA(3);
        // stackArrList.pushA(1);


        s1.pushL(1);
        s1.pushL(2);
        s1.pushL(3);
        s1.pushL(4);
        s1.pushL(5);
        s1.pushL(6);

        s1.popL();
        s1.peekL();

        while(!s1.isempty()){
            System.out.println(s1.peekL());
            s1.popL();
        }

        // while(!s.IsEmpty()){
        //     System.out.println(s.peekA());
        //     s.popA();
        // }

    }

}

