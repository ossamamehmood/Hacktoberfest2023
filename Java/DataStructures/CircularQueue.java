public class CircularQueue {
    static int arr[];
    static int size;
    static int front = -1;
    static int rear = -1;

    CircularQueue(int n) {
        arr = new int[n];
        size = n;
    }

    public static boolean isEmpty() {
        return front == -1 && rear == -1;
    }

    public static boolean isFull() {
        return (rear + 1) % size == front;
    }

    public static void add(int data) {
        if (isFull()) {
            System.out.println("Queue is full. Cannot add " + data);
        } else if (isEmpty()) {
            front = rear = 0;
            arr[rear] = data;
        } else {
            rear = (rear + 1) % size;
            arr[rear] = data;
        }
    }

    public static int remove() {
        int removedItem;
        if (isEmpty()) {
            System.out.println("Queue is empty. Cannot remove.");
            return -1;
        } else if (front == rear) {
            removedItem = arr[front];
            front = rear = -1;
        } else {
            removedItem = arr[front];
            front = (front + 1) % size;
        }
        return removedItem;
    }

    public static int peek() {
        if (isEmpty()) {
            System.out.println("Queue is empty. Cannot peek.");
            return -1;
        }
        return arr[front];
    }

    public static void printQueue() {
        if (isEmpty()) {
            System.out.println("Queue is empty.");
            return;
        }
        int current = front;
        while (true) {
            System.out.print(arr[current] + " ");
            if (current == rear) {
                break;
            }
            current = (current + 1) % size;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        CircularQueue queue = new CircularQueue(5);

        queue.add(1);
        queue.add(2);
        queue.add(3);
        queue.add(4);
        queue.printQueue();

        int removedItem = queue.remove();
        System.out.println("Removed item: " + removedItem);
        queue.printQueue();

        queue.add(5);
        queue.printQueue();
    }
}
