#include <iostream>
using namespace std;

struct node
{
    int data;
    struct node *link;
};

void LinkedListTraversal(struct node *p);
struct node *insertStart(struct node *head, int data);
struct node *insertAtIndex(struct node *head, int data, int index);
struct node *Delete(struct node *head, int index);
struct node *DeleteByValue(struct node *head, int data);

int main()
{
    struct node *head, *first, *second;
    head = new node;
    first = new node;
    second = new node;

    head->data = 10;
    head->link = first;
    first->data = 20;
    first->link = second;
    second->data = 30;
    second->link = NULL;

    LinkedListTraversal(head);
    cout << endl;
    head = insertStart(head, 1);
    LinkedListTraversal(head);

    cout << endl;
    head = insertAtIndex(head, 69, 2);
    LinkedListTraversal(head);

    cout << endl
         << "After Deletion: ";
    head = Delete(head, 2);
    LinkedListTraversal(head);

    return 0;
}

void LinkedListTraversal(struct node *p)
{
    while (p != NULL)
    {
        cout << p->data << " ";
        p = p->link;
    }
}

struct node *insertStart(struct node *head, int data)
{
    struct node *ptr = new node;
    ptr->data = data;
    ptr->link = head;
    return ptr;
}

struct node *insertAtIndex(struct node *head, int data, int index)
{
    if (index < 0)
    {
        cout << "Invalid index." << endl;
        return head;
    }

    struct node *ptr = new node;
    struct node *p = head;
    int i = 0;

    while (i != index - 1 && p != NULL)
    {
        p = p->link;
        i++;
    }

    if (p == NULL)
    {
        cout << "Invalid index." << endl;
        return head;
    }

    ptr->data = data;
    ptr->link = p->link;
    p->link = ptr;

    return head;
}

struct node *Delete(struct node *head, int index)
{
    if (index < 0)
    {
        cout << "Invalid index." << endl;
        return head;
    }

    if (index == 0)
    {
        struct node *temp = head;
        head = head->link;
        delete temp;
        return head;
    }

    struct node *p = head;
    struct node *q = nullptr;
    int i = 0;

    while (i != index && p != NULL)
    {
        q = p;
        p = p->link;
        i++;
    }

    if (p == NULL)
    {
        cout << "Invalid index." << endl;
        return head;
    }

    q->link = p->link;
    delete p;
    return head;
}

struct node *DeleteByValue(struct node *head, int data)
{
    struct node *p = head;
    struct node *q = head->link;
    while (p->data != data && p->link != NULL)
    {
        p = p->link;
        q = q->link;
    }
    if (q->data == data)
    {
        p->link = q->link;
        delete q;
    }
    return head;
}