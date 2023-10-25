#include <stdio.h>
#include <stdlib.h>

typedef struct node{
    int data;
    struct node *next;
}node;

void view(node **);
void insertAtStart(node **, int);
void insertAtEnd(node **, int);
void insertAfter(node **, int, int);
void insertBefore(node **, int, int);
void delHead(node **);
void delEnd(node **);
void delNode(node **, int);
void alterDel(node **);


int main() {
    node *head;
    int c,val,k;
    while(1)
    {
        printf("1.display list\n2.insert at head\n3.insert at tail\n4.insert before value\n5.insert after value\n6.delete head\n7.delete end\n8.delete node\n9.delete alternate\n");
        scanf("%d",&c);
        switch (c) {
            case 1:
                view(&head);
                break;
            case 2:
                printf("enter value: ");
                scanf("%d",&val);
                insertAtStart(&head,val);
                break;
            case 3:
                printf("enter value: ");
                scanf("%d",&val);
                insertAtEnd(&head,val);
                break;
            case 4:
                printf("enter value and k: ");
                scanf("%d%d",&val,&k);
                insertBefore(&head,val,k);
                break;
            case 5:
                printf("enter value and k: ");
                scanf("%d%d",&val,&k);
                insertAfter(&head,val,k);
                break;
            case 6:
                delHead(&head);
                break;
            case 7:
                delEnd(&head);
                break;
            case 8:
                printf("enter value: ");
                scanf("%d",&val);
                delNode(&head, val);
                break;
            case 9:
                alterDel(&head);
                break;

            default:
                printf("invalid");
        }
    }
    return 0;
}
node *createNode(int val){
    node *temp = (node *) malloc(sizeof(node));
    temp->data = val;
    temp->next = NULL;
    return temp;
}

void view(node **head)
{
    node *itr = *head;
    while(itr != NULL)
    {
        printf("%d ",itr->data);
        itr = itr->next;
    }
    printf("\n");
}

void insertAtStart(node **head, int val){
    node *temp = createNode(val);
    if(temp == NULL){
        printf("Memory not allocated!!");
        return;
    }
    if(*head == NULL){
        *head = temp;
        return;
    }
    temp->next = *head;
    *head = temp;
}

void insertAtEnd(node **head, int val){
    node *temp = createNode(val);
    if(temp == NULL){
        printf("Memory not allocated!!");
        return;
    }
    if(*head == NULL){
        *head = temp;
        return;
    }
    node *itr = *head;
    while(itr->next!=NULL)
        itr=itr->next;
    itr->next = temp;
}

void insertAfter(node **head, int val, int k) {
    node *temp = createNode(val);
    if (temp == NULL) {
        printf("Memory not allocated!!");
        return;
    }
    if (*head == NULL) {
        *head = temp;
        return;
    }
    node *itr = *head;
    while (itr->next != NULL && itr->data != k)
        itr = itr->next;
    if (itr->data == k) {
        temp->next = itr->next;
        itr->next = temp;
    }
}

void insertBefore(node **head, int val, int k) {
    node *temp = createNode(val);
    if (temp == NULL) {
        printf("Memory not allocated!!");
        return;
    }
    if (*head == NULL) {
        *head = temp;
        return;
    }
    if ((*head)->data == k){
        temp->next= *head;
        *head = temp;
        return;
    }
    node *itr = *head;
    while (itr->next != NULL && itr->next->data != k)
        itr = itr->next;
    if (itr->next != NULL) {
        temp->next = itr->next;
        itr->next = temp;
        return;
    }
    itr->next = temp;
}

void delHead(node **head)
{
    if(*head == NULL)
        return;
    node *temp = *head;
    if((*head)->next==NULL)
    {
        free(temp);
        *head=NULL;
        return;
    }
    *head = (*head)->next;
    free(temp);
}

void delEnd(node **head)
{
    if(*head == NULL)
        return;
    node *temp = *head;
    if((*head)->next==NULL)
    {
        free(temp);
        *head=NULL;
        return;
    }
    node *itr = *head;
    while(itr->next->next!=NULL)
    {
        itr=itr->next;
    }
    temp=itr;
    itr=itr->next;
    temp->next = NULL;
    free(itr);
}

void delNode(node **head, int val) {
    if (*head == NULL)
        return;
    node *temp = *head;
    if ((*head)->next == NULL) {
        free(temp);
        *head = NULL;
        return;
    }
    if ((*head)->data == val) {
        *head = (*head)->next;
        free(temp);
        return;
    }
    node *itr = *head;
    while (itr->next != NULL && itr->next->data != val) {
        itr = itr->next;
    }
    if (itr->next->data == val) {
        temp = itr->next;
        itr->next = itr->next->next;
        free(temp);
    }
}

void alterDel(node **head)
{
    if(*head ==NULL)
    {
        return;
    }
    if((*head)->next == NULL)
    {
        free(*head);
        *head = NULL;
        return;
    }
    node *temp = *head;
    *head=(*head)->next;
    free(temp);
    temp=NULL;
    node *itr = *head;
    while (itr != NULL && itr->next != NULL)
    {
        temp = itr->next;
        itr->next = itr->next->next;
        free(temp);
        itr=itr->next;
    }
}
