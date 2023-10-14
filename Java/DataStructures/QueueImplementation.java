import java.util.*;
public class QueueImplementation {
    static public class QueueArray{
        static int array[];
        static int size;
        static int rear = -1;

        QueueArray(int n){
            array = new int[n];
            this.size=n;
        }

        public static boolean isEmpty(){
            return rear==-1;
        }

        public static void add(int data){
            if(rear==size-1){
                System.out.println("Queue is Full");
                return;
            }
            rear++;
            array[rear] = data;
        }

        public static int remove(){
            if(isEmpty()){
                System.out.println("List is already Empty");
                return -1;
            }
           
            int front = array[0];
            for(int i=0;i<rear;i++){
                array[i] = array[i+1];
            }

            rear--;
            return front;

        }

        public static int peek(){
            if(isEmpty()){
                System.out.println("List is already Empty");
                return -1;
            }
            return array[0];
        }


    }
    public static void main(String[] args) {
        QueueArray q = new QueueArray(5);
        // q.add(5);
        q.add(1);
        q.add(2);
        q.add(3);
        q.add(4);
        q.remove();

        while(!q.isEmpty()){
            System.out.println(q.peek());
            q.remove();
        }
    }
}
