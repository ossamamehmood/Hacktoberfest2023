#include <iostream>
using namespace std;

// Define a structure for a binary tree node
typedef struct node
{
    int data;
    int height;
    node *left;
    node *right;
} node;

// Initialize the root of the tree as NULL
node *root = NULL;

// Create a class for the AVL Tree
class tree
{
public:
    // Function to get the height of a node
    int getheight(node *n)
    {
        if (n == NULL)
            return 0;
        return n->height;
    }

    // Function to return the maximum of two integers
    int max(int a, int b)
    {
        return (a > b) ? a : b;
    }

    // Function to create a new node with the given data
    node *createnode(int data)
    {
        node *nn = new node;
        nn->data = data;
        nn->left = NULL;
        nn->right = NULL;
        nn->height = 1;
        return nn;
    }

    // Function to get the balance factor of a node
    int getbalancefactor(node *n)
    {
        if (n == NULL)
            return 0;
        return (getheight(n->left) - getheight(n->right));
    }

    // Function to perform a right rotation
    node *rightrotate(node *y)
    {
        node *x = y->left;
        node *t2 = x->right;

        x->right = y;
        y->left = t2;
        y->height = max(getheight(y->right), getheight(y->left));
        x->height = max(getheight(x->right), getheight(x->left));
        return x;
    }

    // Function to perform a left rotation
    node *leftrotate(node *x)
    {
        node *y = x->right;
        node *t2 = y->left;

        y->left = x;
        x->right = t2;
        y->height = max(getheight(y->right), getheight(y->left));
        x->height = max(getheight(x->right), getheight(x->left));
        return y;
    }

    // Function to create a node in the AVL tree
    node *create(node *node, int data)
    {
        if (node == NULL)
            return createnode(data);
        if (data < node->data)
            node->left = create(node->left, data);
        else if (data > node->data)
            node->right = create(node->right, data);
        else // Equal keys not allowed
            return node;
        int bf = getbalancefactor(node);
        if (bf > 1 && data < node->left->data)
            return rightrotate(node);

        // Right Right Case
        if (bf < -1 && data > node->right->data)
            return leftrotate(node);
        // Left Right Case
        if (bf > 1 && data > node->left->data)
        {
            node->left = leftrotate(node->left);
            return rightrotate(node);
        }

        // Right Left Case
        if (bf < -1 && data < node->right->data)
        {
            node->right = rightrotate(node->right);
            return leftrotate(node);
        }
        return node;
    }

    // Function to perform an inorder traversal of the AVL tree
    void inorder(node *root)
    {
        if (root != NULL)
        {
            inorder(root->left);
            cout << root->data << " ";
            inorder(root->right);
        }
    }

    // Function to display the elements in ascending order (inorder)
    void display()
    {
        int ch;
        node *temp = root;
        
        cout << "Data in ascending order (inorder): ";
        inorder(temp);
        cout << endl;
    }

    // Function to search for an element in the AVL tree
    void search()
    {
        int d;
        cout << "Enter data to be searched: ";
        cin >> d;
        node *temp = root, *parent;
        while (temp != NULL)
        {
            if (temp->data == d)
            {
                break;
            }
            else
            {
                parent = temp;
                if (d < temp->data)
                {
                    temp = temp->left;
                }
                else
                {
                    temp = temp->right;
                }
            }
        }
        if (temp == NULL)
        {
            cout << "Element not found\n";
        }
        else
        {
            cout << "Element found\n";
        }
    }
};

int main()
{
    int ch, data;
    tree t;
    do
    {
        cout << "***********************Options************************\n";
        cout << "1.CREATE\n2.DISPLAY\n3.SEARCH\n0.EXIT\n";
        cin >> ch;
        switch (ch)
        {
        case 1:
            cout << "Enter data: ";
            cin >> data;
            root = t.create(root, data);
            break;
        case 2:
            t.display();
            break;
        case 3:
            t.search();
            break;
        case 4:
            return 0;
        case 0:
            break;
        default:
            cout << "INVALID INPUT!!!!";
            break;
        }
    } while (ch);
}
