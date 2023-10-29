/*
    Author : Rohit-110
*/
#include <bits/stdc++.h>
using namespace std;
struct Queue{
    int front,rear,size=0,capacity,*array;
};
Queue* createQueue(int capacity){
	Queue* q = new Queue();
	q->capacity = capacity;
	q->front = q->size = 0;
	q->rear = capacity - 1;
	q->array = new int[q->capacity];
	return q;
}
int isFull(Queue* q){
	return (q->size == q->capacity);
}
int isEmpty(Queue* q){
	return (q->size == 0);
}
void enqueue(Queue* q, int x){
	if (isFull(q)){
	    cout<<"Queue is FULL"<<endl;
		return;
	}
	q->rear = (q->rear + 1)% q->capacity;
	q->array[q->rear] = x;
	q->size = q->size + 1;
}
int dequeue(Queue* q){
	if (isEmpty(q)){
	    cout<<"Queue is empty"<<endl;
	    return INT_MIN;
	}
	int x = q->array[q->front];
	q->front = (q->front + 1)% q->capacity;
	q->size = q->size - 1;
	return x;
}
int front(Queue* q){
	if (isEmpty(q))return INT_MIN;
	return q->array[q->front];
}
int rear(Queue* q){
	if (isEmpty(q))return INT_MIN;
	return q->array[q->rear];
}
int main(){
	Queue* queue = createQueue(1000);
	int n;
	cout<<"Enter the no. elements to insert in queue"<<endl;
	cin>>n;
  cout<<"Enter elements"<<endl;
	for(int i=0;i<n;i++){
	    int x;
	    cin>>x;
	    enqueue(queue,x);
	}
	cout << "Front item of the Queue is "<< front(queue) << endl;
	cout << "Rear item is of the Queue is "<< rear(queue) << endl;
	while(queue->size){
	    cout<<dequeue(queue)<<" ";
	}
	return 0;
}
