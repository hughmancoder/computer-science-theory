#include <iostream>
using namespace std;

class BST {
  int data;
  BST *left, *right;

public:
  BST() : data(0), left(NULL), right(NULL) {}

  BST(int val) {
    data = val;
    left = right = NULL;
  }

  BST *insert(BST *root, int val) {
    if (!root)
      return new BST(val); // make new node

    if (val > root->data) {
      root->right = insert(root->right, val);
    } else {
      root->left = insert(root->left, val);
    }
    return root;
  }

  void inorder(BST *root) // traversal
  {
    if (!root)
      return;
    inorder(root->left);
    cout << root->data << " ";
    inorder(root->right);
  }
};

int main() {
  BST tree, *root = NULL;
  root = tree.insert(root, 2);
  root = tree.insert(root, 10);
  root = tree.insert(root, 9);
  root = tree.insert(root, 4);
  root = tree.insert(root, 6);
  root = tree.insert(root, 8);
  root = tree.insert(root, 5);
  root = tree.insert(root, 3);
  root = tree.insert(root, 7);

  tree.inorder(root);
  return 0;
}
