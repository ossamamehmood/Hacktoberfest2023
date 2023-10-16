
// implementation of queue
#include <bits/stdc++.h>
using namespace std;

// A struct for queue
class Queue {
public:
	int front, rear, size;
	unsigned capacity;
	int* array;
};

// function to create a queue
Queue* createQueue(unsigned capacity)
{
	Queue* queue = new Queue();
	queue->capacity = capacity;
	queue->front = queue->size = 0;


	queue->rear = capacity - 1;
	queue->array = new int[queue->capacity];
	return queue;
}

// to check if queue if full
int isFull(Queue* queue)
{
	return (queue->size == queue->capacity);
}

// to check if queue is empty
int isEmpty(Queue* queue)
{
	return (queue->size == 0);
}

// function to add item in the queue
void enqueue(Queue* queue, int item)
{
	if (isFull(queue))
		return;
	queue->rear = (queue->rear + 1)
				% queue->capacity;
	queue->array[queue->rear] = item;
	queue->size = queue->size + 1;
	cout << item << " enqueued to queue\n";
}

// function to remove item from the queue
int dequeue(Queue* queue)
{
	if (isEmpty(queue))
		return INT_MIN;
	int item = queue->array[queue->front];
	queue->front = (queue->front + 1)
				% queue->capacity;
	queue->size = queue->size - 1;
	return item;
}

// function to get front item from the queue
int front(Queue* queue)
{
	if (isEmpty(queue))
		return INT_MIN;
	return queue->array[queue->front];
}

// function to get rear item from the of queue
int rear(Queue* queue)
{
	if (isEmpty(queue))
		return INT_MIN;
	return queue->array[queue->rear];
}

// Driver code
int main()
{
	Queue* queue = createQueue(1000);

	enqueue(queue, 10);
	enqueue(queue, 20);
	enqueue(queue, 30);
	enqueue(queue, 40);

	cout << dequeue(queue)
		<< " dequeued from queue\n";

	cout << "Front item is "
		<< front(queue) << endl;
	cout << "Rear item is "
		<< rear(queue) << endl;

	return 0;
}


