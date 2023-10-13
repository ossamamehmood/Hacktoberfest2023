#include<iostream>
#include<conio.h>
using namespace std;
struct Node{
	int data;
	Node* next;
};
Node* front = NULL;
Node* rear = NULL;
void display(){
	if( rear == NULL && front == NULL ){
		cout<<"No element in the queue display"<<endl;
		return;
	}
	cout<<"Queue is: ";
	Node *temp = front;
	while(temp != NULL){
		cout<<temp->data<<" ";
		temp = temp->next;
	}
	cout<<endl;
}
void enqueue(int x){
	Node *temp = new Node;
	temp->data = x;
	temp->next = NULL;
	if( front == NULL && rear == NULL ){
		front = rear = temp;
		display();
		return;
	}
	rear->next = temp;
	rear = temp;
	display();
}
void dequeue(){
	Node *head = front;
	if(front == rear){
		cout<<"Deleted Element: "<<front->data<<endl;;
		rear = front = NULL;
		delete head;
		return;
	}
	cout<<"Deleted Element: "<<front->data<<endl;;
	front = front->next;
	delete(head);
	display();
}

int main(){
	display();
	enqueue(5);
	enqueue(6);
	dequeue();
	dequeue();
	display();
}