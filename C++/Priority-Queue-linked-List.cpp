#include<iostream>
using namespace std;
class node
{
public:
	int data;
	node* next;
    int priority;
    node(int n,int p)
	{
		data = n;
        priority = p;
        next = NULL;

	}
};
class Queue
{
    public:
        node *front;
        node *rear;
    
    Queue()
    {
        front = NULL;
        rear = NULL;

    }
    bool Enque(int n,int p)
    {
       node* new_node = new node(n,p);
		if (rear == NULL)
		{
			rear = new_node;
            front = new_node;
        }
		else
		{
            rear->next = new_node;
            rear = new_node;
        }
    }
    int Dequeu()
    {
        if(isEmpty()==true)
        {
            cout << "Queue is Empty!" << endl;
            return 0;

        }
        else
        {

            int temp = front->data;
            node *p = front;
            front = front->next;
            delete p;
            return temp;

        }
    }

    void display()
    {
        node *temp = front;
        while(temp!=NULL)
        {
            cout << temp->data << "  ";
            temp = temp->next;
        }
    }
    bool isEmpty()
    {
        return front == NULL;
    }
 void SortinAsceding() {
        if (front == NULL || front->next == NULL) {
           
			
            return;
        }

        bool swapped;
        do {
            swapped = false;
            node* prev = NULL;
            node* current = front;
            node* nextNode = front->next;

            while (nextNode != NULL) {
                if (current->priority > nextNode->priority) {
                    // Swap current and nextNode values.
                    int temp = current->data;
                    current->data= nextNode->data;
                    nextNode->data = temp;

                    int temp2 = current->priority;
                    current->priority= nextNode->priority;
                    nextNode->priority= temp2;

                    swapped = true;
                }

                prev = current;
                current = nextNode;
                nextNode = nextNode->next;
            }
        } while (swapped);
    
}
   int highestpriority()
   {

     SortinAsceding();
     int v= Dequeu();
     return v;

   }


};
int main(){
    Queue object;
    object.Enque(50,1);
     object.Enque(60,2);
     object.Enque(70,2);
     object.Enque(20,1);
     object.Enque(10, 14);
      object.Enque(9, 3);
       object.Enque(40, 8);
     cout << "current queue is : ";
     object.display();
     cout << endl;
     cout<<object.highestpriority()<<endl;
      object.display();
      cout<<object.highestpriority()<<endl;
      cout << object.highestpriority() << endl;
}
