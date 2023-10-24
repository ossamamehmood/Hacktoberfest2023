#Implementing circular queue in C++

class CircularQueue{
    int *queue;
    int front;
    int rear;
    int size;

    public:
    // Initializing the queue data structure.
    CircularQueue(int n){
        size = n;
        queue = new int[size];
        front = rear = -1;
    }

    // Enqueues 'element' into the queue. Returns true if it gets pushed into the stack and false otherwise.
    bool enqueue(int value){
        //condition to check queue is full 
        if( (front == 0 && rear == size-1) || (rear == (front-1)%(size-1) ) ) {
            cout << "Queue is Full";
            return false;
        }
        else if(front == -1) //to push 1st element
        {
			front = rear = 0;

        }
        else if(rear == size-1 && front != 0) {
            rear = 0; //for mainataing cyclic nature
        }
        else
        {
            rear++;
        }
        //pushing inside the queue
        queue[rear] = value;

        return true;
    }

    // Dequeues top element from queue. Returns -1 if the stack is empty, otherwise returns the popped element.
    int dequeue(){
        if(front == -1){//condition to check queue is empty
            cout << "Queue is Empty " << endl;
            return -1;
        }
        int ans = queue[front];
        queue[front] = -1;
        if(front == rear) {     //only one  element is present
            front = rear = -1;
        }
        else if(front == size - 1) {
            front = 0; //to maintain cyclic nature
        }
        else
        {
            front++;
        }
        return ans;
    }
};

