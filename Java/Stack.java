class Stack {

     class Node {
         int data;
         Node next;
         Node(int d) {
             this.data=d;
             next=null;
         }
     }
     public Node head;
     public  boolean isEmpty() {
      
         return head==null;
       
     }
     public  void push(int data) {
       
        Node newNode = new Node(data);
        if(isEmpty()) {
         head =newNode;
        }
        newNode.next = head;
        head = newNode;
     }
     public int peek() {
         if(isEmpty()) {
             return -1;
         }
         return head.data;
     }
     public int pop() {
         if(isEmpty()) {
             return -1;
         }
        
        int r = head.data;
         head= head.next;
         return r;
        
     }
     public static void main(String[] args) {
         Stack r = new Stack();
         r.push(1);
         r.push(2);
         r.push(3);
         r.push(4);
         for(int i=1;i<5;i++) {
             System.out.println(r.peek());
             r.pop();
         }
       
     }

    
 } 
