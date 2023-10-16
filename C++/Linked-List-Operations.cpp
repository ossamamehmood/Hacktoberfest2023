#include <iostream>
using namespace std;

// class for Node
class node {
    public:
    int data;
    node* next;
};

// printing an Linked List
void Print(node* head){
    node* ptr = head;
    if(head==NULL){
        cout<<"Linked List is empty";
    }else{
        do{
            cout<<ptr->data<<" ";
            ptr=ptr->next;
        }while(ptr!=NULL);
    }
    cout<<endl;
}

// inserting an element in a Linked List

//insert at head
void insertHead(node* &head,int val){
    if(head==NULL){
        node* new_node= new node();
        new_node->data=val;
        head=new_node;
        new_node->next=NULL;
    }else{
        node* new_node= new node();
        new_node->data=val;
        new_node->next=head;
        head=new_node;
    }
    
}

//insert at tail
void insertTail(node* head, int val){
    node* ptr = head;
    node* new_node= new node();
    new_node->data=val;
    while(ptr->next!=NULL){
        ptr=ptr->next;
    }
    ptr->next=new_node;
}

// insert before a given val
void insertBefore(node* head,int key,int val){
    node* ptr = head;
    while(ptr->next->data!=key){
        if(ptr->next->next==NULL){
            cout<<"key not found - insertBefore key("<<key<<")"<<endl;
            return;                
        }
        ptr=ptr->next;
    }
    node* new_node= new node();
    new_node->data=val;
    new_node->next=ptr->next;
    ptr->next = new_node;
}

//insert after a given val
void insertAfter(node* head,int key,int val){
    node* ptr = head;
    while(ptr->data!=key){
        if(ptr->next==NULL){
            cout<<"key not found - insertAfter key("<<key<<")"<<endl;
            return;
        }
        ptr=ptr->next;
    }
    node* new_node = new node();
    new_node->data=val;
    new_node->next=ptr->next;
    ptr->next=new_node;
}

//delete a given element
void Delete(node* &head,int key){
    node* ptr = head;
    if(ptr->data==key){
        node* temp=ptr;
        head=ptr->next;
        free(temp);
        return;
    }
    while(ptr->next->data!=key){
        if(ptr->next->next==NULL){
            cout<<"key not found - Delete key("<<key<<")"<<endl;
            return;
        }
        ptr=ptr->next;
    }
    node* temp=ptr->next;
    ptr->next = ptr->next->next;
    free(temp);
}

//search a element in a Linked List
void Search(node* head,int key){
    node* ptr = head;
    while(ptr->data!=key){
        if(ptr->next==NULL){
            cout<<"key not found - search key("<<key<<")"<<endl;
            return;
        }
        ptr=ptr->next;
    }
    cout<<"key found"<<endl;
}

int main(){
    node*head=NULL;
    insertHead(head,4);
    insertHead(head,5);
    insertHead(head,0);
    insertTail(head,9);
    insertTail(head,11);
    insertBefore(head,5,1);
    insertBefore(head,1,6);
    insertAfter(head,1,8);
    insertAfter(head,6,3);
    Print(head);
    Delete(head,9);
    Delete(head,6);
    Search(head,8);
    Search(head,7);
    Print(head);
}
