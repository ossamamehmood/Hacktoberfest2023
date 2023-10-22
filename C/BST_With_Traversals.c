#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

typedef struct TreeNode {
    int data;
    struct TreeNode* left;
    struct TreeNode* right;
}TreeNode;

typedef struct Queue {
    TreeNode** arr;
    int size;
    int front;
    int rear;
}Queue;

TreeNode* create_node(int data) {
    TreeNode* n = (TreeNode*)malloc(sizeof(TreeNode));
    n->data = data;
    n->left = NULL;
    n->right = NULL;
    return n;
}

Queue* create_queue(int size) {
    Queue* q = (Queue*)malloc(sizeof(Queue));
    q->size = size;
    q->arr = (TreeNode**)malloc(size*sizeof(TreeNode*));
    q->front = -1;
    q->rear = -1;
    return q;
}

bool isEmpty(Queue* queue) {
    if(queue->front==-1)
        return true;
    else
        return false;
}

bool isFull(Queue* queue) {
    if((queue->rear+1)%queue->size==queue->front)
        return true;
    else
        return false;
}

void push(Queue* queue, TreeNode* node) {
    if(isFull(queue))
        printf("Queue is full!");
    else {
        if(queue->front==-1) {
            queue->front++;
            queue->front %= queue->size;
        }
        queue->rear++;
        queue->rear %= queue->size;
        queue->arr[queue->rear] = node;
    }
}

TreeNode* pop(Queue* queue) {
    if(isEmpty(queue))
        return NULL;
    else {
        TreeNode* popped = queue->arr[queue->front];
        if(queue->front==queue->rear) {
            queue->front = queue->rear = -1;
        }
        else {
            queue->front++;
            queue->front %= queue->size;
        }
        return popped;
    }
}

TreeNode* front(Queue* queue) {
    if(queue->front==-1)
        return NULL;
    return queue->arr[queue->front];
}

TreeNode* rear(Queue* queue) {
    if(queue->rear==-1)
        return NULL;
    return queue->arr[queue->rear];
}

void levelOrderTraversal(TreeNode* root) {
    if(root==NULL)
        return;
    Queue* queue = create_queue(10);
    push(queue, root);
    push(queue, NULL);
    while(!isEmpty(queue)) {
        TreeNode* temp = front(queue);
        pop(queue);
        if(temp!=NULL) {
            printf("%d ", temp->data);
            if(temp->left!=NULL)
                push(queue, temp->left);
            if(temp->right!=NULL)
                push(queue, temp->right);
        }
        else {
            printf("\n");
            if(!isEmpty(queue)) {
                push(queue, NULL);
            }
        }
    }
}

void preorderTraversal(TreeNode* root) {
    if(root==NULL)
        return;

    printf("%d ", root->data);
    preorderTraversal(root->left);
    preorderTraversal(root->right);
}

void inorderTraversal(TreeNode* root) {
    if(root==NULL)
        return;

    inorderTraversal(root->left);
    printf("%d ", root->data);
    inorderTraversal(root->right);
}

void postOrderTraversal(TreeNode* root) {
    if(root==NULL)
        return;

    postOrderTraversal(root->left);
    postOrderTraversal(root->right);
    printf("%d ", root->data);
}

TreeNode* constructBST(TreeNode* root, int val) {
    if(root==NULL)
        return create_node(val);
    
    if(val<root->data)
        root->left = constructBST(root->left, val);
    else
        root->right = constructBST(root->right, val);

    return root;
}


int main() {
    int data, ch;
    printf("Enter data for the root : ");
    scanf("%d", &data);
    TreeNode* root = NULL;
    root = constructBST(root, data);
    while(true) {
        printf("Enter data for another node? Press 1 for yes, 0 for no:");
        scanf("%d", &ch);
        if(ch==0)
            break;
        printf("Enter data:");
        scanf("%d", &data);
        root = constructBST(root, data);
    }
    printf("\nPreoder traversal : ");
    preorderTraversal(root);
    printf("\n\nInorder traversal : ");
    inorderTraversal(root);
    printf("\n\nPostorder traversal : ");
    postOrderTraversal(root);
    printf("\n\nLevel-order traversal : \n");
    levelOrderTraversal(root);
    printf("\n");
    return 0;
}
