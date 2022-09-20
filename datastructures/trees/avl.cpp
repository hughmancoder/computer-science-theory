#include <iostream>
#include <string>
#include <sstream>
#include <queue>
#include <stack>

class Node {
    public:
        Node *left, *right;
        int height; 
        int val;
        // constructor
        Node (int val):left(NULL), right(NULL), height(1), val(val){}
};

int height(Node *node);
int getBalanceFactor(Node* node);
Node* rightRotate(Node *p);
Node* leftRotate(Node *p);
Node* insert(Node* node, int value);
Node* Delete(Node* root, int value);

void preorder(Node* node, Node* root);
void inorder(Node* node, Node* root);
void postorder(Node* node, Node* root);
void iterativePreorder(Node* root);
void iterativeInorder(Node* root);
void iterativePostorder(Node* root);


void demo() {
    Node* root = NULL;
    root = insert(root, 10);
    root = insert(root, 3);
    root = insert(root, 100);
    root = insert(root, -3);
    root = insert(root, 42);
    root = insert(root, 0); 
    root = insert(root, 3242); 
    root = insert(root, -234); 
    
    root = Delete(root, 0); 
    root = Delete(root, -234);
    root = Delete(root, 10);

    std::cout << "Inorder traversal ";
    inorder(root, root);

    std::cout << "\nPreorder traversal ";
    preorder(root, root);

    std::cout << "\nPostorder traversal ";
    postorder(root, root);
}

int main() {
    Node* root = NULL;
    std::string str;
    std::getline(std::cin, str);
    std::istringstream ss(str);
    std::string s;
    // std::cout << "input is: " << str << std::endl;
    while (ss >> s) {
        if (s == "PRE") {
            // preorder(root, root);
            // std::cout << std::endl;
            std::cout << "root value: " << root->val << std::endl;
            iterativePreorder(root);
            break;
        }
        else if (s == "IN") {
            // inorder(root, root);
            // std::cout << std::endl;
            iterativeInorder(root);
            break;
        }
        else if (s == "POST") {
            // postorder(root, root);
            // std::cout << std::endl;
            iterativePostorder(root);
            break;
        }
        else if (s.size() > 1 and s[0] == 'A') {
            std::string number = s.substr(1);
            // std::cout << "Inserting " << number << " into tree" << std::endl;
            root = insert(root, std::stoi(number));
        }
        else if (s.size() > 1 and s[0] == 'D') {
            std::string number = s.substr(1);
            // std::cout << "Deleting " << number << " from tree" << std::endl;
            root = Delete(root, std::stoi(number));
        }
    }
    return 0;
}

int height(Node *node)
{
    if (node == NULL)
        return 0;
    return node->height;
}

// left - right height
int getBalanceFactor(Node* node) {
    return node == NULL ? 0 : (height(node->left) - height(node->right));
}

// gets next largest node: smallest key greater than input node
Node* getSuccessor(Node *node) {
    Node* temp = node; // get copy so we don't directly modify node itself
    if (temp->right) {
        temp = temp->right;
        while (temp->left) {
            temp = temp->left;
        }
    }
    return temp;
}


Node *leftRotate(Node *p) {
    Node *r = p->right;
    Node *rl = r->left;

    p->right = rl;
    r->left = p;
    
    // update heights of repositioned nodes
    p->height = std::max(height(p->left), height(p->right) + 1);
    r->height = std::max(height(r->left), height(r->right) + 1);
    // r becomes the new parent
    return r;
}

Node* rightRotate(Node *p) {
    Node *l = p->left;
    Node *lr = l->right;

    p->left = lr;
    l->right = p;
    
    // update heights of repositioned nodes
    p->height = std::max(height(p->left), height(p->right) + 1);
    l->height = std::max(height(l->left), height(l->right) + 1);
    // l becomes the new parent
    return l;
}

Node *insert(Node *node, int value) {
    if (node == NULL) {
        return new Node(value);
    }

    if(value < node->val) {
        node->left = insert(node->left, value);
    }
    else if(value > node->val) {
        node->right = insert(node->right, value);
    }
    // value equal to root value so return node as equal keys are not allowed
    else { 
        return node;
    }

    node->height = 1 + std::max(height(node->left), height(node->right));
    int balance_factor = getBalanceFactor(node);
    // left left case
    if (balance_factor > 1 && value < node->left->val) {
        return rightRotate(node);
    }
    // right right case
    if (balance_factor < -1 && value > node->right->val) {
        return leftRotate(node);
    }
    // left right case
    if (balance_factor > 1 && value > node->left->val) {
        node->left = leftRotate(node->left);
        return rightRotate(node);
    }
    // right left case
    if (balance_factor < -1 && value < node->right->val) {
        node->right = rightRotate(node->right);
        return leftRotate(node);
    }
    return node;
}

Node *Delete(Node* root, int value) {
    // 1) BST deletion
    if (!root) return root; 
    else if(value < root->val) { // search through tree to find match of node we want to delete
        root->left = Delete(root->left, value);
    }
    else if(value > root->val) {
        root->right = Delete(root->right, value);
    }
    else {        
        // node has no children
        if (!root->right and !root->left) {
            root = NULL;
        }
        // node has one child
        else if (!root->left or !root->right) {
            // replace root with connecting node (which deletes root)
            Node* node_to_connect = root->left ? root->left : root->right;
            root = node_to_connect;
        }
        else { // node has two children
            Node* successor = getSuccessor(root);
            // printf("successor value of %d is %d\n",root->val, successor->val);
            // make successor as the new root node of subtree (pivot)
            root->val = successor->val;
            // Delete the inorder successor
            root->right = Delete(root->right, successor->val);
        }
    }
    // if tree only has 1 node we delete that node and return NULL
    if (root == NULL) {
        return root;
    }
    // 2) update height of current node
    root->height = 1 + std::max(height(root->left), height(root->right));
    // 3) get balance factor and balance accordingly
    int balance_factor = getBalanceFactor(root);
    // left left case
    if (balance_factor > 1 and getBalanceFactor(root->left) >= 0) {
        return rightRotate(root);
    }
    // right right case
    if (balance_factor < -1 and getBalanceFactor(root->right) <= 0) {
        return leftRotate(root);
    }
    // left right case
    if (balance_factor > 1 and getBalanceFactor(root->left) < 0) {
        root->left = leftRotate(root->left);
        return rightRotate(root);
    }
    // right left case
    if (balance_factor < -1 and getBalanceFactor(root->right) > 0) {
        root->right = rightRotate(root->right);
        return leftRotate(root);
    }
    return root;
}

// recursive functions
void preorder(Node* node, Node* root) {
    if (!root) {
        std::cout << "EMPTY ";
        return;
    }
    else if(!node) { 
        return;
    }
    std::cout << node->val << " ";
    preorder(node->left, root);
    preorder(node->right, root); 
}

void inorder(Node* node, Node* root) {
    if (!root) {
        std::cout << "EMPTY ";
        return;
    }
    else if(!node) { 
        return;
    }
    inorder(node->left, root);
    std::cout << node->val << " ";
    inorder(node->right, root); 
}

void postorder(Node* node, Node* root) {
    if (!root) {
        std::cout << "EMPTY ";
        return;
    }
    else if(!node) { 
        return;
    }
    postorder(node->left, root);
    postorder(node->right, root); 
    std::cout << node->val << " ";
}

// iterative functions 
void iterativePreorder(Node* root) {
    if (!root) return;
    std::stack<Node*> stk;
    Node* curr;
    stk.push(root);
    while (!stk.empty()) {
        curr = stk.top(), stk.pop();
        if (curr != nullptr) {
            std::cout << curr->val << " ";
            stk.push(curr->right);
            stk.push(curr->left); 
        }
    }
}

void iterativeInorder(Node* root) {
    if (!root) return;
    std::stack<Node*> s;
    Node* curr = root;
    while (curr != NULL || s.empty() == false) {
        while (curr !=  NULL) {
            s.push(curr);
            curr = curr->left;
        }
        std::cout << s.top()->val << " ";
        curr = s.top()->right;
        s.pop();
    }
}

void iterativePostorder(Node* root) {
    if (!root) return;
    std::stack<Node*> stk;
    Node* last = NULL;
    while (!stk.empty() || root) {
        if (root) { 
            stk.push(root); // push all valid roots to stack
            root = root->left; // 1. go to left
        }
        else {
            Node* node = stk.top();
            if(node->right && node->right != last) {
                root = node->right; // 2. go to right
            }
            else {
                std::cout << node->val << " ";
                last = node; // needed to prevent infinite cycleback
                stk.pop();
            }
        }
    }
}
