//Circular Doubly Linked List Menu Driven PRogram
#include<stdio.h>
#include<stdlib.h>
struct individualnode
 {
    int value;
    struct individualnode* nextnode;
    struct individualnode* prevnode;
};
void deletion_right(struct individualnode** top)
{
    
    if((*top)==NULL)
    {
        printf("\nList does not exist\n");//there is no list
        return;
    }
   struct individualnode *last=(*top)->prevnode;
   struct individualnode*last1=last->prevnode;
   if(*top==last)
   {
        free(*top);
        *top=NULL;
        return;
   }
   last1->nextnode=*top;
   (*top)->prevnode=last1;
   free(last);//free the memory location
}
void add_after_k(struct individualnode** top,int element, int givenelement)
{
     struct individualnode*Temporary=(struct individualnode*)malloc(1*sizeof(struct individualnode));
    if(Temporary==NULL)
    {
        printf("Memory allocation failed");//To Check if the memory was sucessfully allocated
        return;
    }
    Temporary->value=element;
    if((*top)==NULL)
    {
        Temporary->nextnode=Temporary;
        Temporary->prevnode=Temporary;//there is no list
        *top=Temporary;
        return;
    }
    struct individualnode*current=*top;
    do
    {
        if(current->value==givenelement)//current  is used to traverse through the list
        {
            Temporary->nextnode=current->nextnode;
            Temporary->prevnode=current;
            current->nextnode=Temporary;
            Temporary->nextnode->prevnode=Temporary;//element is found in the list
            return;
        }
        current=current->nextnode;
    }while(current!=current->nextnode);
}
void traverse_end(struct individualnode** top)
{
    if((*top)==NULL)
    {
        printf("\nList does not exist\n");//there is no list
        return;
    }
    struct individualnode* last = (*top)->prevnode;
    struct individualnode* current = last;

    do
    {
        printf("%d ,", current->value);//current  is used to traverse through the list
        current = current->prevnode;
    } while (current != last);
}
void add_before_given_element(struct individualnode** top,int element,int givenelement)
{
    struct individualnode*Temporary=(struct individualnode*)malloc(1*sizeof(struct individualnode));
    if(Temporary==NULL)
    {
        printf("Memory allocation failed");//To Check if the memory was sucessfully allocated
        return;
    }
    Temporary->value=element;
    if((*top)==NULL)
    {
        Temporary->nextnode=Temporary;//there is no list
        Temporary->prevnode=Temporary;
        *top=Temporary;
        return;
    }
    struct individualnode*current=*top;
    if(current->value==givenelement)//current  is used to traverse through the list
    {
        Temporary->nextnode=*top;
        Temporary->prevnode=(*top)->prevnode;
        current->prevnode->nextnode=Temporary;//element is found in the list
        *top=Temporary;
        return;
    }
    while(current->nextnode!=*top && current->nextnode->value!=givenelement)//current  is used to traverse through the list
    {
        current=current->nextnode;
    }
    if(current->nextnode==*top && current->value!=givenelement)
    {
        printf("\nElement not found\n",givenelement);
        return;
    }
    Temporary->nextnode=current->nextnode;
    Temporary->prevnode=current;
    current->nextnode=Temporary;
    Temporary->nextnode->prevnode=Temporary;
}
void add_at_right(struct individualnode** top,int element)
{
    struct individualnode*Temporary=(struct individualnode*)malloc(1*sizeof(struct individualnode));
    if(Temporary==NULL)
    {
        printf("Memory allocation failed");//To Check if the memory was sucessfully allocated
        return;
    }
    Temporary->value=element;
    if((*top)==NULL)
    {
        Temporary->nextnode=Temporary;//there is no list
        Temporary->prevnode=Temporary;
        *top=Temporary;
        return;
    }
    struct individualnode*end=(*top)->prevnode; 
    Temporary->nextnode=*top;
    Temporary->prevnode=end;
    end->nextnode=Temporary;
    (*top)->prevnode=Temporary;
}
void deletion_element(struct individualnode** top,int element)
{
    
   if((*top)==NULL)
   {
        printf("\nList does not exist\n");//there is no list
        return;
   }
   struct individualnode*Temporary=*top,*Temporary1=(*top)->nextnode; 
   if(Temporary->value==element)
   {
        if (*top == (*top)->nextnode)//when element is found at top
        {
            free(*top);
            *top=NULL;
            return;
        }
        else
        {
            Temporary1->prevnode=Temporary->prevnode;//element is found in the list
            Temporary->prevnode->nextnode=Temporary1;
            free(Temporary);//free the memory location
            *top=Temporary1;
            return;
        }
   }
        while(Temporary1!=*top)
        {
            if(Temporary1->value==element)
            {
                Temporary->nextnode=Temporary1->nextnode;
                Temporary1->nextnode->prevnode=Temporary;
                free(Temporary1);//free the memory location
                return;
            }
            Temporary=Temporary1;
            Temporary1=Temporary->nextnode;
        }
}  
void add_at_left(struct individualnode** top,int element)
{
    struct individualnode*Temporary=(struct individualnode*)malloc(1*sizeof(struct individualnode));
    if(Temporary==NULL)
    {
        printf("Memory allocation failed");//To Check if the memory was sucessfully allocated
        return;
    }
    Temporary->value=element;
    if((*top)==NULL)
    {
        Temporary->nextnode=Temporary;//there is no list
        Temporary->prevnode=Temporary;
    }
    else
    {
        struct individualnode* end= (*top)->prevnode;
        Temporary->nextnode=*top;
        Temporary->prevnode=end;
        (*top)->prevnode=Temporary;
        end->nextnode=Temporary;
    }
    *top=Temporary;
}
void deletion_left(struct individualnode** top)
{
    if((*top)==NULL)
    {
        printf("\nList does not exist\n");//there is no list
        return;
    }
    struct individualnode*Temporary=(*top)->prevnode;
    struct individualnode*Temporary1=(*top);
    if((*top)==(*top)->prevnode)
    {
        free(*top);
        *top = NULL;
    }
    else
    {
        Temporary->nextnode=(*top)->nextnode;
        (*top)->nextnode->prevnode=Temporary;
        *top=(*top)->nextnode;
        free(Temporary1);//free the memory location
    }
}
void Traverse_start(struct individualnode** top)
{
    if((*top)==NULL)
    {
       printf("\nList does not exist\n");//there is no list
        return;
    }
    struct individualnode *current=*top;//current  is used to traverse through the list
    do
    {
        printf("%d ,", current->value);
        current=current->nextnode;
    }while(current!=(*top));
}
int main()
{
    struct individualnode * top=NULL;
    char character;
    int cases,element,givenelement;
    do//use of do while loop to run the loop one extra time atleast
    {
       printf("input your choice:\n1.Add at left\n2.Add at end\n3.Add before a given value\n4.Add after a given value\n5.Remove a node by value\n6.remove first node\n7.Remove last node\n8.Traverse from Right\n9.Traverse from Left: \n");
       scanf("%d",&cases);
       switch (cases)
       {
            case 1:
            {
                printf("\ninput the element to Add at left: ");
                scanf("%d",&element);
                add_at_left(&top,element);
                break;
            }
            case 2:
            {
                printf("\ninput the element to Add at right: ");
                scanf("%d",&element);
                add_at_right(&top,element);
                break;
            }
            case 3:
            {
                printf("\ninput the element to Add : ");
                scanf("%d",&element );
                printf("\nTO be inserted before which element:");
                scanf("%d",&givenelement);
                add_before_given_element(&top,element,givenelement);
                break;
            }
            case 4:
            {
               printf("\ninput the element to Add : ");
               scanf("%d", &element);             
               printf("\nTO be inserted after which element: ");
               scanf("%d",&givenelement);
               add_after_k(&top,element,givenelement);
               break;
            }
            case 5:
            {
                printf("\nInput Value to be removed from list :");
                scanf("%d",&givenelement);
                deletion_element(&top,givenelement);
                break;
            }
            case 6 :
            {
                deletion_left(&top);
                break;
            }
            case 7:
            {
                deletion_right(&top);
                break;
            }
            case 8:
            {
                Traverse_start(&top);
                break;
            }
            case 9:
            {
                traverse_end(&top);
                break;
            }
            default:
            {
                printf("\nInput VAlid values\n");
            }
        }
        printf("\nto continue: Y-yes or to not continue  N-no: ");
        scanf(" %c",&character);
    }while(character=='y'||character=='Y');
    while (top) 
    {
        struct individualnode* Temporary = top;
        top = top->nextnode;
        free(Temporary);
    }
    return 0;
}