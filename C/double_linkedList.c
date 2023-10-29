//double linked list
#include<stdio.h>
#include<stdlib.h>
struct node
{
    int data;
    struct node* prev, *next;
}*head=NULL, *temp, *new, *temp2;
void creation();
void insertion();
void deletion();
void display();
void search();
void reverse();
int ref = 0;
int main()
{
    int ch;
    while(1)
    {
        printf("enter\n1 to create DLL\n2 to display DLL\n3 to search\n4 to insert a node\n5 to delete\n6 to reverse\n7. to exit\n");
        scanf("%d", &ch);
        if(ch==7)
        {
            break;
        }
        switch (ch)
        {
            case 1:
                creation();
                break;
            case 2:
                display();
                break;
            case 3:
                search();
                break;
            case 4:
                insertion();
                break;
            case 5:
                deletion();
                break;
            case 6:
                reverse();
                break;
            default:
                printf("select corrrect choice\n");
                break;
        }
    }
    return 0;
}
void creation()
{
    while(1)
    {
        int choice, num;
        printf("enter data of node\n");
        scanf("%d", &num);
        new = (struct node *)malloc(sizeof(struct node));
        new->data = num;
        new->prev = NULL;
        new->next = NULL;
        ref++;
        if(head==NULL)
        {
            head = temp = new;
        }
        else
        {
            temp->next = new;
            new->prev = temp;
            temp = new;
        }
        printf("enter\n1 to continue\n0 to stop\n");
        scanf("%d", &choice);
        if(choice==1)
        {
            continue;
        }
        else if(choice==0)
        {
          break;
        }
        else
        {
          printf("enter valid choice\n");
        }
    }
}
void insertion()
{
    int choice, num, pos, i=1;
    if(ref==0)
    {
      printf("linked list is empty. Create the list inorder to insert\n");
      return;
    }
    printf("enter data of node\n");
    scanf("%d", &num);
    new = (struct node *)malloc(sizeof(struct node));
    new->data = num;
    new->prev = NULL;
    new->next = NULL;
    printf("enter\n1 to insert at the start\n2 to insert at the end\n3 to insert at a position\n");
    scanf("%d", &choice);
    switch(choice)
    {
        case 1:
            new->next = head;
            head->prev = new;
            head = new;
            ref++;
            break;
        case 2:
            temp = head;
            while(temp->next!=NULL)
            {
                temp = temp->next;
            }
            temp->next = new;
            new->prev = temp;
            temp = new;
            ref++;
            break;
        case 3:
            printf("enter position\n");
            scanf("%d", &pos);
            if(pos<1 || pos-1>ref)
            {
                printf("enter valid position\n");
            }
            else if(pos==1)
            {
                new->next = head;
                head = new;
                ref++;
            }
            else
            {
                temp = head;
                while(i<pos-1)
                {
                    temp = temp->next;
                    i++;
                }
                temp2 = temp->next;
                temp->next = new;
                new->prev = temp;
                new->next = temp2;
                if(temp2!=NULL)
                {
                    temp2->prev = new;
                }
                ref++;
            }
            break;
        default:
            printf("select correct choice\n");
            break;
    }
}
void deletion()
{
    if(head==NULL)
    {
        printf("linked list is empty\n");
        return;
    }
    int choice, pos, i=1;
    printf("enter\n1 to delete first node\n2 to delete last node\n3 to delete node at a position\n");
    scanf("%d", &choice);
    switch(choice)
    {
        case 1:
            temp = head;
            if(temp->next!=NULL)
            {
                temp->next->prev = NULL;
                head = temp->next;
            }
            free(temp);
            if(ref==1)
            {
                head = NULL;
            }
            ref--;
            break;
        case 2:
            temp = head;
            while(temp->next!=NULL)
            {
                temp = temp->next;
            }
            temp2 = temp;
            if(temp->prev!=NULL)
            {
                  temp->prev->next = NULL;
            }
            free(temp2);
            if(ref==1)
            {
                head = NULL;
            }
            ref--;
            break;
        case 3:
            printf("enter position\n");
            scanf("%d", &pos);
            if(pos<1 || pos>ref)
            {
                printf("enter valid position\n");
            }
            else
            {
                temp = head;
                if(pos==1)
                {
                    temp2 = temp->next;
                    temp2->prev = NULL;
                    head = temp2;
                }
                else
                {
                      while(i<pos)
                      {
                          temp2 = temp;
                          temp = temp->next;
                          i++;
                      }
                      if(pos==ref)
                      {
                          temp2->next = NULL;
                      }
                      else
                      {
                          temp2->next = temp->next;
                          temp->next->prev = temp2;
                      }
                      
                }
                free(temp);
                if(ref==1)
                {
                    head = NULL;
                }
                ref--;
            }
            break;
        default:
            printf("select valid choice\n");
            break;
    }
}
void display()
{
    if(head==NULL)
    {
        printf("linked list is empty\n");
        return;
    }
    temp = head;
    while(temp!=NULL)
    {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}
void search()
{
    if(head==NULL)
    {
        printf("linked list is empty\n");
        return;
    }
    int key;
    printf("enter key value to search\n");
    scanf("%d", &key);
    temp = head;
    while(temp!=NULL)
    {
        if(key==temp->data)
        {
            printf("found\n");
            break;
        }
        temp = temp->next;
    }
    if(temp==NULL)
    {
        printf("not found\n");
    }
}
void reverse()
{
    if(head==NULL)
    {
        printf("linked list is empty\n");
        return;
    }
    temp = head;
    temp2 = temp->next;
    temp->next = NULL;
    temp->prev = temp2;
    while(temp2!=NULL)
    {
        temp2->prev = temp2->next;
        temp2->next = temp;
        temp = temp2;
        temp2 = temp2->prev;
    }
    head = temp;
}