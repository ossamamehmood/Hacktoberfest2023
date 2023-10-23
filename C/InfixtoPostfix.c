#include <stdio.h>
#include <stdbool.h>
#include<string.h>

int top = -1;
int size ;
char stack[50];

bool isEmpty() {
    return top == -1;
}

bool isFull() {
    return top == size - 1;
}

void push(char data) {
    if(isFull()) {
        printf("Stack is full");
    }
   else{
        top++;
        stack[top] = data;
   }
    }

char pop() {
    if(isEmpty()) {
        printf("Stack is empty");

    }
    else{
        char ele = stack[top];
        top--;
        return ele;
        
    }
    
}

void display() {
    for (int i = top; i >= 0; i--) {
       
        printf("%c\n", stack[i]);
    }
}


void infixToPostfix()
{
char infix[100];

printf("Enter your exp: ");
gets(infix);
size= strlen(infix);


char postfix[100];
int j=0;
char symbol;
int precedence(char ch) {
    switch(ch) {
        case '^' :
        return 3;
        break;
        case '*' :
        case '/' :
        return 2;
        break;
        case '+':
        case '-' :
        return 1;
        break;
        default :
        return 0;
    }
}
char next;
for(int i=0;i<strlen(infix);i++) {
    symbol=infix[i];
    switch(symbol) {
        case '(' :
        push(symbol);
        break;
        case ')' :
        while((next=pop())!='(') {
            
            postfix[j] = next;
            j++;
        }
        break;
        case '^' :
        case '*' :
        case '/' :
        case '+' :
        case '-' :
        while(precedence(stack[top]) >= precedence(symbol) && !isEmpty() ) {
            postfix[j] = pop();
            j++;
            
           
        }
        push(symbol);
         break;
       default : 
       postfix[j] = symbol;
       j++;

    }
   
} 
while(!isEmpty())
{
    postfix[j]=pop();
    j++;
}
postfix[j]='\0';
 puts(postfix);
 }



int main() {
   infixToPostfix();
   
   
    
    return 0 ;
}










