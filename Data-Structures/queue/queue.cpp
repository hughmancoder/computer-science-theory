#include <iostream>
using namespace std;

class Node
{
public:
    int data;
    Node *next;
    Node(int val) : data(val), next(NULL){};
};

class queue
{
public:
    Node *front, *end; // public for testing
    queue() : front(NULL), end(NULL) {}

    void enqueue(int val) // endqueue to the end of the linked list
    {
        Node *temp = new Node(val);
        if (end == NULL)
        {
            front = end = temp;
        }
        end->next = temp;
        end = temp;
    }

    void dequeue() // we dequeue from the front of the linked list
    {
        if (front == NULL)
        {
            return;
        }
        Node* temp = front;
        front = front->next;

        if(front == NULL) end = NULL; // if the queue is empty

        delete(temp); // free up memory
    }
};


int main() 
{
    queue *q = new queue();
    q->enqueue(1);
    q->enqueue(2);
    q->enqueue(3);
    q->enqueue(4);
    q->enqueue(5);

    q->dequeue(); // remove front of queue
    q->dequeue();
    cout << "Queue Front : " << (q->front)->data << endl;
    cout << "Queue Rear : " << (q->end)->data << endl;

}