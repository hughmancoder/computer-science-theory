#include <iostream>
using namespace std;

// implementing with a linked list
class Node {
  int data;
  Node *next;
  Node *top_;

public:
  Node() { // creating construtor
    top_ = NULL;
  }

  void push(int data) {
    Node *temp = new Node();
    if (!temp) {
      cout << "stack overflow" << endl;
      return;
    }
    temp->data = data;
    temp->next =
        top_; // add new element to top of stack by linking to previous top
    top_ = temp;
  }

  int isEmpty() { return top_ == NULL; }

  int top() {
    if (!isEmpty())
      return top_->data;
    cout << "stack is empty" << endl;
    return 0;
  }

  void pop() {
    if (top_ == NULL) {
      return;
    }
    Node *temp = top_;
    top_ = top_->next;
    free(temp); // delete memory
  }
};

int main() {
  Node *stack = new Node();
  stack->push(1);
  stack->push(2);
  stack->push(3);
  stack->push(4);
  cout << stack->top() << endl;
  stack->pop();
  cout << stack->top() << endl;

  return 0;
}