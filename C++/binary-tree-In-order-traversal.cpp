// Online C++ compiler to run C++ program online
#include <iostream>

struct TreeNode {
    int data;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int val) : data(val), left(nullptr), right(nullptr) {}
};

class BinaryTree {
public:
    BinaryTree() : root(nullptr) {}

    void insert(int val) {
        root = insertRecursive(root, val);
    }

    void inOrderTraversal() {
        inOrderRecursive(root);
    }

private:
    TreeNode* root;

    TreeNode* insertRecursive(TreeNode* node, int val) {
        if (node == nullptr) {
            return new TreeNode(val);
        }

        if (val < node->data) {
            node->left = insertRecursive(node->left, val);
        } else {
            node->right = insertRecursive(node->right, val);
        }

        return node;
    }

    void inOrderRecursive(TreeNode* node) {
        if (node == nullptr) {
            return;
        }

        inOrderRecursive(node->left);
        std::cout << node->data << " ";
        inOrderRecursive(node->right);
    }
};

int main() {
    BinaryTree tree;
    int values[] = {50, 30, 70, 20, 40, 60, 80};

    for (int val : values) {
        tree.insert(val);
    }

    std::cout << "In-order traversal: ";
    tree.inOrderTraversal();
    std::cout << std::endl;

    return 0;
}
