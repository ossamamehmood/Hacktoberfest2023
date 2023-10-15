public class floyd {
    public static class Node{    
        int data;
        Node next;

        public Node(int data){
        this.data = data;
        this.next = null;
        }
    }
    public static Node head;
    public static Node tail;

    public void addFirst(int data){
        //step1 = create new Node
        Node newNode = new Node(data);
        if(head == null){
            head = tail = newNode;
            return; 
        }
        //step2 = newNode next assigned to next Node
        newNode.next = head;
        // step3 = head assigned to newNode
        head = newNode; 
    }
    public void print(){
        Node temp = head;
        while(temp != null){
            System.out.print(temp.data + "->");
            temp = temp.next;
        }
        System.out.println("null");
    }
    public static boolean cycle(){
        Node fast=head; Node slow = head;

        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
            if(fast == slow){
                return true;
            }
        }
        return false;
    }
    public static void main(String args[]){
        head = new Node(1);
        head.next = new Node(1857);
        head.next.next = new Node(4428);
        head.next.next.next = new Node(132981);
        head.next.next.next.next = new Node(423);

        System.err.println(cycle());
  }
}
