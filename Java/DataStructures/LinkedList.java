public class LinkedList {
    Node head;
    private int size;

    LinkedList(){
        this.size = 0;
    }

    class Node{
        String data;
        Node next;

        Node(String data){
            this.data = data;
            this.next = null;
            size++;
        }
    }

    public void printlist(){
        if(head==null){
            System.out.println("List is Empty");
            return;
        }
        Node currNode = head;
        while(currNode!=null){
            System.out.print(currNode.data + "-> ");
            currNode = currNode.next;
        }
        System.out.println("null");
        
    }

    public void addfirst(String data){
        Node newnode = new Node(data);
        if(head == null){
            head = newnode;
            return;
        }

        newnode.next = head;
        head = newnode;
    }

    public void addlast(String data){
        Node newnode = new Node(data);
        if(head == null){
            head = newnode;
            
        }

        Node lastnode = head;
        if(lastnode.next!=null){
            lastnode = lastnode.next;
        }
        lastnode.next = newnode;
       newnode.next = null;
    }

    public void deletefirst(){
       // Node newnode = head;
        if(head==null){
            System.out.println("List is already Empty");
            return;
        }
        size--;
        head = this.head.next;
    }

    public void deletelast(){
        if(head==null){
            System.out.println("List is Empty");
        }
        size--;

        if(head.next == null){
            head=null;
            return;
        }
        Node currNode = head;
        Node lastnode = head.next;

        if(lastnode.next!=null){
            currNode = currNode.next;
            lastnode = lastnode.next;
        }
        currNode.next = null;

    }

    // public void addatindex(int i){
    //     Node curNode = head.next;
    //     Node prevNode = head;

    //     if(curNode.next!=i)
    // }

    public int getSize(){
        return size;
    }

    // public void reversell(){
    //     if(head==null || head.next==null){
    //         return ;
    //     }
    //     Node prevnode = head;
    //     Node currnode = head.next;
    //     if(currnode!=null){
    //         Node nextnode = currnode.next;
    //         currnode.next = prevnode;

    //         prevnode = currnode;
    //         currnode = nextnode;
    //     }

    //     head.next = null;
    //     head = prevnode;
    // }

    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        // list.addfirst("Datir");
        // list.addfirst("Dev");
        // list.addfirst("I am");
        // list.printlist();
        list.addlast("From");
        list.addlast("Amravati");
        list.addfirst("Dev");
        list.addfirst("Datir");
        list.deletefirst();
        list.deletelast();
        list.deletelast();
        list.addlast("Datir");
        list.printlist();
        
        System.out.println(list.getSize());
    }
}
